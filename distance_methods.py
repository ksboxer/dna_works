# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:54:09 2016

@author: Kate
"""

class DistanceMethods:
    """
    Compute the Damerau-Levenshtein distance between two given
    strings (s1 and s2)
    """
    # method taken for the following website: https://www.guyrutenberg.com/2008/12/15/damerau-levenshtein-distance-in-python/
    # Christopher P. Matthews
# christophermatthews1985@gmail.com
# Sacramento, CA, USA

    def levenshtein(self,s, t):
            ''' From Wikipedia article; Iterative with two matrix rows. '''
            if s == t: return 0
            elif len(s) == 0: return len(t)
            elif len(t) == 0: return len(s)
            v0 = [None] * (len(t) + 1)
            v1 = [None] * (len(t) + 1)
            for i in range(len(v0)):
                v0[i] = i
            for i in range(len(s)):
                v1[0] = i + 1
                for j in range(len(t)):
                    cost = 0 if s[i] == t[j] else 1
                    v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
                for j in range(len(v0)):
                    v0[j] = v1[j]
                    
            return v1[len(t)]