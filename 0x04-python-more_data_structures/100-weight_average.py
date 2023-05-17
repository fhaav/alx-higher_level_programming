#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list) and all(isinstance(t, tuple) and
                                         len(t) == 2 for t in my_list):
        if len(my_list) == 0:
            return 0
        scores_sum = sum(score * weight for score, weight in my_list)
        weights_sum = sum(weight for _, weight in my_list)
        return scores_sum / weights_sum
    else:
        return 0
