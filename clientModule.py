# @Author: Atul Sahay <atul>
# @Date:   2019-07-09T12:13:14+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2019-07-09T13:07:07+05:30

import numpy as np

def cosine_sim(vec1,vec2):
    dot = np.dot(vec1, vec2)
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    cos = dot / (norma * normb)
    return cos
