class NeuralNetUtils:
    @staticmethod
    def get_levels(pred):
        threshold = 0.5

        flag_start = False
        global_position_level = []
        accumulator = []
        score = 0
        for i in range(pred.shape[1]):
            if pred[0,i,0,0] > threshold:
                if flag_start == False:
                    flag_start = True
                    accumulator = [i]
                    score = pred[0,i,0,0]
                else:
                    accumulator.append(i)
                    score += pred[0,i,0,0]
            else:
                if flag_start == True:
                    flag_start = False
                    center = accumulator[len(accumulator)//2]
                    height = accumulator[-1]-accumulator[0]
                    score = score / len(accumulator)
                    global_position_level.append({'center':center, 'height':height, 'score':score })
        return global_position_level

    @staticmethod
    def get_foam(pred):
        threshold = 0.5

        flag_start = False
        global_position_level = []
        start_point = 0
        end_point = 0
        score = 0
        for i in range(pred.shape[1]):
            if pred[0,i,0,0] > threshold:
                if flag_start == False:
                    flag_start = True
                    start_point = i
                    score = pred[0,i,0,0]
                else:
                    score += pred[0,i,0,0]
            else:
                if flag_start == True:
                    flag_start = False
                    end_point = i
                    score = score / (end_point-start_point)
                    global_position_level.append({'start_pt':start_point, 'end_pt':end_point, 'score':score })
        return global_position_level

    @staticmethod
    def are_levels_valid(levels, min_limit, max_limit):
        return len(levels) > 0 and levels[-1]['center'] > min_limit and levels[-1]['center'] < max_limit