# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:18:30 2020

@author: duher18
"""


from __future__ import division
from nbgrader.plugins import BasePlugin


class SubMarks(BasePlugin):
    def late_submission_penalty(self, student_id, score, total_seconds_late):
        """Penalty of 1 mark per hour late"""
        # hours_late = total_seconds_late / 3600
        # return round(hours_late, 0)
    
        """Machine Vision penalty policy"""
        if total_seconds_late == 0:
            return score*0
        elif total_seconds_late > 0 and total_seconds_late <= 172800: # 0-2 days
            return score*0.25
        elif total_seconds_late > 172800 and total_seconds_late <= 345600: # 2-4 days
            return score*0.5
        elif total_seconds_late > 345600 and total_seconds_late <= 518400: # 4-6 days
            return score*0.75
        else:
            return score*1