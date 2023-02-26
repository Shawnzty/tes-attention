import numpy as np

def make_trials(num1, code1, num2, code2):
    trial = np.concatenate((code1*np.ones(num1, dtype=int), code2*np.ones(num2, dtype=int)))
    np.random.shuffle(trial)
    return trial