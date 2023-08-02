# --------------------------------------------
#   Name: Kashish Mittal
#   ID: 1638174
#   CMPUT 274, Fall 2020
#
#   Assignment 1: OO Classifier
# --------------------------------------------
# Copyright 2020 Paul Lu
import sys
import copy  # for deepcopy()

Debug = False  # Sometimes, print for debugging
InputFilename = "input.file.v1"
TargetWords = [
    'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
    'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
    'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
    '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
]


def get_wordcount(words):
    """ Creates a dictionary of all the words and their counts
    which appear in the words and sorts them based on values
    from greatest to lowest and then stores them as word-count
    pairs in the wordlist

    :Arguments: words: a list of words
    :return: word_list: A list of word-count pairs
    """
    dict_words = dict()
    # iterating through word element in words
    for word in words:
        # iterating through each element in word
        for element in word:
            # Checking to see if the element already exists
            # as a key in the dictionary if it does we add
            # 1 to its value
            if element in dict_words.keys():
                dict_words[element] = dict_words.get(element) + 1
            # if does not exist we create a new key as the word
            # and set its value as 1
            else:
                dict_words[element] = 1
    # we use to sorted function to sort the the dictionary elements by value
    # we set key by using the lambda(one line functions) which creates list of
    # word count pairs and then picks the second element of the list
    # which is the values and sets it as the key and also set
    # reverse = True so the the list is sorted in descending order of value
    word_list = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
    return word_list


def remove_punc_symb(lower_list):
    """ This function is used to remove all punctuations in the words
    :Argument: lower_list: A list containing words
    :return: A list containing words without punctuation
    """
    new_list = []
    temp = ""
    # Used to iterate through each word in the lower_list
    for i in lower_list:
        # Used to iterate character by character of the word
        for j in i:
            # Checks if the character is a alphabet or digit
            # if it is then we add it to temp string
            if j.isalnum() == 1:
                temp += j
        # After checking each character we append it to another list
        new_list.append(temp)
        temp = ""
    return new_list


def remove_digits(lower_list):
    """ This function is used to remove all digits in the word except
    when the word only contains digits
    :Argument: lower_list: A list consisting of words
    :return: A list containing words with digits removed
    """
    new_list = []
    temp = ""
    # Used to iterate through each word in list
    for i in lower_list:
        # If the entire word consist of only digits we append it to
        # new_list
        if i.isdecimal():
            new_list.append(i)
        else:
            # Used to iterate character by character of the word
            for j in i:
                # Check to see if the character is not a digit
                # if condition satisfies we add to temp
                if j.isdigit() == 0:
                    temp += j
            # After checking each character we append it to another list
            new_list.append(temp)
            temp = ""
    return new_list


def remove_stopword(lower_list):
    """ This function is used to remove all the stop words from
    the list
    :Arguments: lower_list: A list consisting of words
    :return: new_list: A list containing words with stopwords removed
    """
    new_list = []
    # Creating a list of all the stopwords
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
                 "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
                 "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
                 "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
                 "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                 "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
                 "or", "because", "as", "until", "while", "of", "at", "by", "for", "with",
                 "about", "against", "between", "into", "through", "during", "before", "after",
                 "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
                 "under", "again", "further", "then", "once", "here", "there", "when", "where",
                 "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                 "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                 "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    # Used to iterate through each word in the list
    for i in lower_list:
        # Checks whether the word is not in the stopword list
        # if it is we append it to new_list
        if i not in stopwords:
            new_list.append(i)
    return new_list


def keep_digits(lower_list):
    """ This functions is used to remove all the symbols and punctuation
    and also remover all the stopwords
    ::Argument: lower_list: A list consisting of words
    :return: new_list: A list
    """
    new_list = remove_punc_symb(lower_list)
    new_list = remove_stopword(new_list)
    return new_list


def keep_symbols(lower_list):
    """ This functions is used to remove the digits and remove all the
    stopwords
    :Argument: lower_list: A list consisting of words
    :return: new_list: A list
    """
    new_list = remove_digits(lower_list)
    new_list = remove_stopword(new_list)
    return new_list


def keep_stops(lower_list):
    """ This functions is used to remove the digits and remove all the
    symbols and punctuation
    :Argument: lower_list: A list consisting of words
    :return: new_list: A list
    """
    new_list = remove_punc_symb(lower_list)
    new_list = remove_digits(new_list)
    return new_list


def removeall(lower_list):
    """ This functions is used to remove the digits, remove all the
    symbols and punctuation and also remove all the stopwords
    :Argument: lower_list: A list consisting of words
    :return: new_list: a list
    """
    new_list = remove_punc_symb(lower_list)
    new_list = remove_digits(new_list)
    new_list = remove_stopword(new_list)
    return new_list


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return (f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return (sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return (sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return ("", False)
        return (line.strip(), True)
    except EOFError:
        return ("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return (self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return (s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        # FIXME:  Call superclass, here and for all classes
        self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    def get_TF(self):
        return (self.TP, self.FP, self.TN, self.FN)

    # FIXME:  Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return (self.targetWords)

    def get_allWords(self):
        return (self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return (self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return (self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords Hardcoded (%d): " % ln, end='')
        print(self.get_target_words())
        return

    def print_run_info(self):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag + "-------- Confusion Matrix --------")
        print(tag + "%10s | %13s" % ('Predict', 'Label'))
        print(tag + "-----------+----------------------")
        print(tag + "%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag + "%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag + "%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag + "%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag + "%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():  # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w  # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return (inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return (cl, e)


class ClassifyByTopN(ClassifyByTarget):
    def __init__(self, lw=[]):
        self.type = str(self.__class__)
        super().__init__(lw)
        return

    #   Compare with classify_all() in class TrainingSet
    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return

    def target_top_n(self, tset, num=5, label=''):
        """ This method is use to pick the target words based on
        frequency

        :Argument: tset: a object of class TrainingSet

        :Argument: num: an integer used to specify number of target
        words we need to pick. Default value is 5

        :Argument: label: A string used to provide us with the label
        default value is ''(empty string)
        """
        words = []
        lw = []
        # get all the instances from tset
        instances = tset.get_instances()
        # iterate through all the instances
        for i in instances:
            # check to see if the label of the instance matches
            # the label passed as parameter
            # if it does we append the words from that instance
            # to the words
            if i.get_label() == label:
                words.append(i.get_words())
        words_list = get_wordcount(words)
        #for i in range(len(words_list)):
            # check to remove the label from word list
            # as the label occurs all the time it has the highest
            # count so we remove it using pop
            #if words_list[i][0] == label:
               # words_list.pop(i)
                #break

        for i in range(num):
            lw.append(words_list[i][0])
        # picking the value of num'th word
        v = words_list[num - 1][1]
        # checking to see if the word after num have the same value
        # if they do we append it to word_list
        for j in range(num, len(words_list)):
            if words_list[j][1] == v:
                lw.append(words_list[j][0])
        self.set_target_words(lw)
        return


class TrainingInstance(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"  # Class, given by oracle
        self.inst["words"] = []  # Bag of words
        self.inst["class"] = ""  # Class, by classifier
        self.inst["explain"] = ""  # Explanation for classification
        self.inst["experiments"] = dict()  # Previous classifier runs
        return

    def get_label(self):
        return (self.inst["label"])

    def get_words(self):
        return (self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):  # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return ("N/A")
        else:
            return (cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return ("N/A")
        else:
            return (cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
            self, line, run=None,
            tlabel="read", inclLabel=True
    ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                # FIXME: For testing only.  Compare to previous version.
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return (self)

    def preprocess_words(self, mode=''):
        """ This method is used process words based on the value of
        mode which is passed as parameter.
        :Argument: mode: A string. Default value is '' empty string
        """
        # iterating through all the words and converting them to
        # lower case
        for i in range(len(self.get_words())):
            self.inst["words"][i] = self.inst["words"][i].lower()
        # Check to see the value of mode and perform function based
        # on that
        if mode == 'keep-symbols':
            self.inst["words"] = keep_symbols(self.get_words())
        elif mode == 'keep-digits':
            self.inst["words"] = keep_digits(self.get_words())
        elif mode == 'keep-stops':
            self.inst["words"] = keep_stops(self.get_words())
        else:
            self.inst["words"] = removeall(self.get_words())
        return


class TrainingSet(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inObjList = []  # Unparsed lines, from training set
        self.inObjHash = []  # Parsed lines, in dictionary/hash
        return

    def get_instances(self):
        return (self.inObjHash)  # FIXME Should protect this more

    def get_lines(self):
        return (self.inObjList)  # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")  # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            # Check for comments
            if line[0] == '%':  # Comments must start with %
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=''):
        """This is method calls the preprocess_words() and perform
        all the preprocessing actions for all training instances
        in a particular dataset

        :Argument: mode: string, used to specify the mode. Default
        value is '' empty string
        """
        instances = self.get_instances()
        # calls prepocess_words() on all instances in the dataset
        for i in instances:
            i.preprocess_words(mode)
        return

    def return_nfolds(self, num=3):
        """This method is used to divide the dataset in num-folds
        and return a lsit of num objects of class TrainingSet.

        :Argument: num: An integer used to specify the number of
        folds/partition we need to make of the dataset. Default
        value is 3

        :return: tfold: a list consisting on num objects of class
        TrainingSet
        """
        tfold = []
        # using nested loops so we can divide the dataset equally
        for j in range(num):
            # we create a deepcopy of the object which calls this
            # method and store it as the elemet on tfold
            tfold.append(self.copy())
            # we then clear both inObjHash as well as the inObjList
            # so that we can store new values there
            tfold[j].inObjHash.clear()
            tfold[j].inObjList.clear()
            # then we run a for loop with jumps of num and append the
            # values of inObjHash and inObjList using get_instances()
            # and get_lines respectively
            for i in range(j,len(self.get_instances()),num):
                tfold[j].inObjHash.append(self.get_instances()[i])
                tfold[j].inObjList.append(self.get_lines()[i])
        return tfold

    def copy(self):
        """This method is used to create a deepcopy of object which
        calls it
        :return:tset_copy: a deepcopy of the object which calls this
        method
        """
        tset_copy = copy.deepcopy(self)
        return tset_copy

    def add_fold(self, tset):
        """This method is used to add the training instances of tset
        to an object of class TrainingSet

        :Arguments: tset: an object of class TrainingSet
        """
        # create a deepcopy of tset
        new_tset = tset.copy()
        # iterate through all the training instances and lines
        # and append them to inObjHash and inObjList respectively
        for i in range(len(new_tset.get_instances())):
            self.inObjHash.append(new_tset.get_instances()[i])
            self.inObjList.append(new_tset.get_lines()[i])
        return


def basemain():
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    print(run1)  # Just to show __str__
    lr = [run1]
    print(lr)  # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:  # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, '#weather')

    return


if __name__ == "__main__":
    basemain()
