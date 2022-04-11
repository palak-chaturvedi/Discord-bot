import asyncio
import random
import re
import os


# todo: probably need to remove punctuation from answers


class Quiz:

    def __init__(self, client, win_limit=10, hint_time=30):
        # initialises the quiz
        self.__running = False
        self.current_question = None
        self._win_limit = win_limit
        self._hint_time = hint_time
        self._questions = []
        self._asked = []
        self.scores = {}
        self._client = client
        self._quiz_channel = None
        self._cancel_callback = True

        # load in some questions
        datafiles = os.listdir('quizdata')
        for df in datafiles:
            filepath = 'quizdata' + os.path.sep + df
            self._load_questions(filepath)
            print('Loaded: ' + filepath)
        print('Quiz data loading complete.\n')

    def _load_questions(self, question_file):
        # loads in the questions for the quiz
        with open(question_file, encoding='utf-8', errors='replace') as qfile:
            lines = qfile.readlines()

        question = None
        category = None
        answer = None
        regex = None
        position = 0

        while position < len(lines):
            if lines[position].strip().startswith('#'):
                # skip
                position += 1
                continue
            if lines[position].strip() == '':  # blank line
                # add question
                if question is not None and answer is not None:
                    q = Question(question=question, answer=answer,
                                 category=category, regex=regex)
                    self._questions.append(q)

                # reset everything
                question = None
                category = None
                answer = None
                regex = None
                position += 1
                continue

            if lines[position].strip().lower().startswith('category'):
                category = lines[position].strip()[lines[position].find(':') + 1:].strip()
            elif lines[position].strip().lower().startswith('question'):
                question = lines[position].strip()[lines[position].find(':') + 1:].strip()
            elif lines[position].strip().lower().startswith('answer'):
                answer = lines[position].strip()[lines[position].find(':') + 1:].strip()
            elif lines[position].strip().lower().startswith('regexp'):
                regex = lines[position].strip()[lines[position].find(':') + 1:].strip()
            # else ignore
            position += 1

    def started(self):
        # finds out whether a quiz is running
        return self.__running

    def question_in_progress(self):
        # finds out whether a question is currently in progress
        return self.__current_question is not None

    async def _hint(self, hint_question, hint_number):
        # offers a hint to the user
        if self.__running and self.current_question is not None:
            await asyncio.sleep(self._hint_time)
            if (self.current_question == hint_question
                    and self._cancel_callback == False):
                if (hint_number >= 5):
                    await self.next_question(self._channel)

                hint = self.current_question.get_hint(hint_number)
                await self._client.send_message(self._channel, 'Hint {}: {}'.format(hint_number, hint))
                if hint_number < 5:
                    await self._hint(hint_question, hint_number + 1)

    async def start(self, channel):
        # starts the quiz in the given channel.
        if self.__running:
            # don't start again
            await self._client.send_message(channel,
                                            'Quiz already started in channel {}, you can stop it with !stop or !halt'.format(
                                                self._channel.name))
        else:
            await self.reset()
            self._channel = channel
            await self._client.send_message(self._channel, '@here Quiz starting in 10 seconds...')
            await asyncio.sleep(10)
            self.__running = True
            await self.ask_question()

    async def reset(self):
        if self.__running:
            # stop
            await self.stop()

        # reset the scores
        self.current_question = None
        self._cancel_callback = True
        self.__running = False
        self._questions.append(self._asked)
        self._asked = []
        self.scores = {}

    async def stop(self):
        # stops the quiz from running
        if self.__running:
            # print results
            # stop quiz
            await self._client.send_message(self._channel, 'Quiz stopping.')
            if (self.current_question is not None):
                await self._client.send_message(self._channel,
                                                'The answer to the current question is: {}'.format(
                                                    self.current_question.get_answer()))
            await self.print_scores()
            self.current_question = None
            self._cancel_callback = True
            self.__running = False
        else:
            await self._client.send_message(self._channel, 'No quiz running, start one with !ask or !quiz')

    async def ask_question(self):
        # asks a question in the quiz
        if self.__running:
            # grab a random question
            qpos = random.randint(0, len(self._questions) - 1)
            self.current_question = self._questions[qpos]
            self._questions.remove(self.current_question)
            self._asked.append(self.current_question)
            await self._client.send_message(self._channel,
                                            'Question {}: {}'.format(len(self._asked),
                                                                     self.current_question.ask_question()))
            self._cancel_callback = False
            await self._hint(self.current_question, 1)

    async def next_question(self, channel):
        # moves to the next question
        if self.__running:
            if channel == self._channel:
                await self._client.send_message(self._channel,
                                                'Moving onto next question. The answer I was looking for was: {}'.format(
                                                    self.current_question.get_answer()))
                self.current_question = None
                self._cancel_callback = True
                await self.ask_question()

    async def answer_question(self, message):
        # checks the answer to a question
        if self.__running and self.current_question is not None:
            if message.channel != self._channel:
                pass

            if self.current_question.answer_correct(message.content):
                # record success
                self._cancel_callback = True

                if message.author.name in self.scores:
                    self.scores[message.author.name] += 1
                else:
                    self.scores[message.author.name] = 1

                await self._client.send_message(self._channel,
                                                'Well done, {}, the correct answer was: {}'.format(message.author.name,
                                                                                                   self.current_question.get_answer()))
                self.current_question = None

                # check win
                if self.scores[message.author.name] == self._win_limit:

                    await self.print_scores()
                    await self._client.send_message(self._channel,
                                                    '{} has won! Congratulations.'.format(message.author.name))
                    self._questions.append(self._asked)
                    self._asked = []
                    self.__running = False

                    # print totals?
                elif len(self._asked) % 5 == 0:
                    await self.print_scores()

                await self.ask_question()

    async def print_scores(self):
        # prints out a table of scores.
        if self.__running:
            await self._client.send_message(self._channel, 'Current quiz results:')
        else:
            await self._client.send_message(self._channel, 'Most recent quiz results:')

        highest = 0
        for name in self.scores:
            await self._client.send_message(self._channel, '{}:\t{}'.format(name, self.scores[name]))
            if self.scores[name] > highest:
                highest = self.scores[name]

        if len(self.scores) == 0:
            await self._client.send_message(self._channel, 'No results to display.')

        leaders = []
        for name in self.scores:
            if self.scores[name] == highest:
                leaders.append(name)

        if len(leaders) > 0:
            if len(leaders) == 1:
                await self._client.send_message(self._channel, 'Current leader: {}'.format(leaders[0]))
            else:
                await self._client.send_message(self._channel, 'Print leaders: {}'.format(leaders))


class Question:
    # A question in a quiz
    def __init__(self, question, answer, category=None, author=None, regex=None):
        self.question = question
        self.answer = answer
        self.author = author
        self.regex = regex
        self.category = category
        self._hints = 0

    def ask_question(self):
        # gets a pretty formatted version of the question.
        question_text = ''
        if self.category is not None:
            question_text += '({}) '.format(self.category)
        else:
            question_text += '(General) '
        if self.author is not None:
            question_text += 'Posed by {}. '.format(self.author)
        question_text += self.question
        return question_text

    def answer_correct(self, answer):
        # checks if an answer is correct or not.

        # should check regex
        if self.regex is not None:
            match = re.fullmatch(self.regex.strip(), answer.strip())
            return match is not None

        # else just string match
        return answer.lower().strip() == self.answer.lower().strip()

    def get_hint(self, hint_number):
        # gets a formatted hint for the question
        hint = []
        for i in range(len(self.answer)):
            if i % 5 < hint_number:
                hint = hint + list(self.answer[i])
            else:
                if self.answer[i] == ' ':
                    hint += ' '
                else:
                    hint += '-'

        return ''.join(hint)

    def get_answer(self):
        # gets the expected answer
        return self.answer