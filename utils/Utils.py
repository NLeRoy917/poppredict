class Utils:
    """
    Utility class with some common manipulations and methods
    """
    def __init__(self):
        pass

    def int_to_key(self,key_int):
        '''
        Convert a integer key value to the actual key. Spotify only provides the integer value,
        so the actual key must be hard-coded in.
        '''
        if key_int == 0:
        	key = 'C'
        elif key_int == 1:
        	key = 'C#'
        elif key_int == 2:
        	key = 'D'
        elif key_int == 3:
        	key = 'D#'
        elif key_int == 4:
        	key = 'E'
        elif key_int == 5:
        	key = 'F'
        elif key_int == 6:
        	key = 'F#'
        elif key_int == 7:
        	key = 'G'
        elif key_int == 8:
        	key = 'G#'
        elif key_int == 9:
        	key = 'A'
        elif key_int == 10 or key_int == 't':
        	key = 'A#'
        elif key_int == 11 or key_int == 'e':
        	key = 'B'
        else:
        	key = 'no_key'
         
        return key
    
    def int_to_mode(self,mode_int):
        '''
        convert the mode integer to minor or major
        '''
        if mode_int == 0:
        	mode = 'Minor'
        elif mode_int == 1:
        	mode = 'Major'
        else:
        	mode = 'No Mode'

        return mode
    
    def int_to_time_signature(self,time_sig_int):
        '''
        convert time signature int value to time signature
        '''

        if time_sig_int == 3:
        	time_sig = '3/4'
        elif time_sig_int == 4:
        	time_sig = '4/4'
        elif time_sig_int == 5:
        	time_sig = '5/4'
        elif time_sig_int == 6:
        	time_sig = '6/4'
        elif time_sig_int == 7:
        	time_sig = '7/4'
        elif time_sig_int == 1:
        	time_sig = 'Complex'
        else:
            time_sig = 'None'
        return time_sig