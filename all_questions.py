import pytest
from all_questions import *
import pickle


#-----------------------------------------------------------
def question1():
    answers = {}


    # type: float
    # Calculate the probability.
    # P(B=Good,F=Empty,G=Empty,S=yes) = P(B=good)⋅P(F=empty)⋅P(G=empty∣B=good,F=empty)⋅P(S=yes∣B=good,F=empty)
    P_B_bad = .1
    P_B_good = .9
    P_F_empty = .2
    P_F_notempty = .8
    P_G_empty_given_B_good_F_empty = .8
    P_S_no_given_B_good_F_empty = .8
    P_S_yes_given_B_good_F_empty = .2

    a = P_B_good * P_F_empty * P_G_empty_given_B_good_F_empty * P_S_yes_given_B_good_F_empty
    # print(a)

    answers['(a)'] = a

    # type: float
    # Calculate the probability.
    # P(B=bad,F=empty,G=not empty,S=no)P(B=bad,F=empty,G=not empty,S=no) = P(B=bad)⋅P(F=empty)⋅P(G=not empty∣B=bad,F=empty)⋅P(S=no∣B=bad,F=empty)
    P_G_empty_given_B_bad_F_empty = 0.9
    P_G_notempty_given_B_bad_F_empty = 0.1
    P_S_no_given_B_bad_F_empty = 1
    b = P_B_bad * P_F_empty * P_G_notempty_given_B_bad_F_empty * P_S_no_given_B_bad_F_empty
    # print(b)
    answers['(b)'] = b

    # type: float
    # Calculate the probability.
    # Compute P(S = yes | B = bad)
    P_S_yes_given_B_bad_F_notempty = 1
    P_S_yes_given_B_bad_F_empty = 0
    P_G_empty_given_B_bad_F_notempty = 0.2
    P_G_empty_given_B_bad_F_empty = 0.9
    c = P_F_empty * P_G_empty_given_B_bad_F_empty * P_S_yes_given_B_bad_F_empty + P_F_notempty * P_G_empty_given_B_bad_F_notempty * P_S_yes_given_B_bad_F_notempty#value of first term should be zero
    # print(c)
    answers['(c)'] = c
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False


    

    


    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.

    # Only one round of boosting, so the normalization factor will not affect the weight in this case.
    # alpha = 0.5 * np.log((1 - error_rate) / error_rate) Will suffice 

    answers['(c) Weight update'] = "1/2 * math.log((1 - p) / p)" 
    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528 #calculated from exp(alpha)
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "no"

    # type: explain_string
    answers['Explain'] = "Flipping a coin is a random process that does not actually have any predictive power over/relative to the stock market. Conceptually, a 50/50 coin flip does not have any sort of predictive power."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = True

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float

    # Assuming p <= .5?
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "p"

    # type: eval_float
    answers['(a) C1-FPR'] = "2*p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "No"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Since both C1 and C2 lie on the line of TPR = FPR, niether classifier is better than the other."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) explain'] = "When considering precision and recall, C2 seems like the better option since the it correctly classifies more true positives. However, that metric is not really indicitave of the overall performance of the classifiers, as it only really highlights the trade off between the two (more true positives with the tradeoff of more false positives). TPR/FPR, in the other hand, gives more of a complete picture of the classifiers in this case. Since both models have the same TPR/FPR ratio, neither is really better than the other overall in distinguishing between the classes."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "While both C1 and C2 have the same precision, C2 has a much higher recall and F1-measure, which indicates that it is better at identifying positive cases than C1."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "While TPR-FPR is fine, it is limited in scope as it does not take into account the precision of the classifiers. Precision, recall, and F1-measure does do this, as well as balancing the metrics of precision and recall."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "In terms of wanting to avoid false positives would prefer C3, as it has a higher precision than the rest of the classifiers (on top of having the least sacrifice in recall and F1-measure in its performance compared to C1 and C2)."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "1/10" # 100p/1000p, which is True Positive / Total predictions

    # type: eval_float
    answers['(a) recall for C0'] = "p" # Expected number of true positives is 100p, and the number of actual positives is 100.

    # type: eval_float
    answers['(b) F-measure of C0'] = "(0.2*p)/(.1+p)" # Harmonic mean of precision and recall. 2 * (Precision*Recall/(Precision+Recall)) = .2p/(.1 + p)

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'yes' # Under the assumption that p is the proportion of the positive class in the dataset (0.1). F-Measure = (.2 * .1)/(.1 + .1) = 0.1. Since the F1-Measure of C0 (.1) is less than that of C1 (.15), C1 is a better random classifier. This is still an assumption though.

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3 # Solving for p in F-Measure of C0 = .15 gives p = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    precision = 80/(80+70)
    recall = 80/(80 + 50)
    f1_measure = 2 * ((precision*recall)/(precision+recall))
    accuracy = (80 + 800)/(80 + 800 + 50 + 70)
    answers['(i) metrics'] = {

        'recall': recall,

        'precision': precision,

        'F-measure': f1_measure,

        'accuracy': accuracy

    }


    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'accuracy' 

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'F-measure'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "Accuracy is definitely the best metric, as it accurately shows the overall correctness and performance of the algorithm. The worst metric would probably be F measure, as it doesnt give any new information beyond what precision and recall give (which already dont do a good job at indicating overall performance), and has a bias towards the positive class."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2" 

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "In the context of detecting cancer, I feel like TPR/FPR's focus on detecting as many potentially positive cases as possible is more important."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "I would reverse my choice if The test failing (leading to a false positive) could lead to significant harm. F1's higher confidence in positive predictions."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
