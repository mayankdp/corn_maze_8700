from abc import ABC, abstractmethod
import string

class Pattern:

    def createMazeWall() -> str:
        raise NotImplementedError()

class One(Pattern):
    def createMazeWall() -> str:
        return """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W                         W               
W   WWWW  WWWWWWWWWW  WW  W    
W   W             W       W       
W   W          WWWWWWWWW  W           
W  WW  WWWW        W   W  W    
W   W     W W      W   W  W       
W   W     W   WWW  W   W  W       
W   WWW WWW   W W  W   W  W       
W     W   W   W W      W  W         
WWW   W   WWWWW W      W  W        
W W      WW       WWWW    W        
W W   WWWW   WWW          W       
W              W  WWWWWWWWW        
WWWWWW  WWWWWWWW          W
W                       E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]

class Two(Pattern):
    def createMazeWall() -> str:
        return """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W                         W               
W   WWWWWWW      WWWWWW   W    
W   W             W       W       
W   W    WWWW  WWWWWWWWW  W           
W  WW                  W  W    
W   W     W   WWWWWWW  W  W       
W   W     W   W        W  W       
W   WWW   W   W        W  W       
W     W   W   W        W  W         
WWW   W   W   W        W  W        
W W      WW       WWWW    W        
W W   WWWWW   WWW         W       
W              W  WWWWWWWWW        
WWWWWWWWWWW               W
W                       E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]

class Three(Pattern):
    def createMazeWall() -> str:
        return """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W   WWWWWWWW              W               
W   WWWWWWWWWWW  WWWWWW   W    
W   W             W       W       
W   W          WWWWWWWWW  W           
W  WWWWWWWWWWWWWWW     W  W    
W   W     W   WWWWWWW  W  W       
W   W     W   W        W  W       
W   WWW   W   W W      W  W       
W     W   W   W W      W  W         
WWW   W   W   W W      W  W        
W W      WW       WWWW    W        
W W   WWWWWW  WWW         W       
W              W  WWWWWWWWW        
WWWWWWWWWWWWWWWW  W       W
W          W            E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]


PATTERN_FACTORY = {
	1: One,
	2: Two,
    3: Three
}

class CreateMazeWall:
    def rise(pattern_type: int):
        new_pattern = PATTERN_FACTORY.get(pattern_type)
        if not new_pattern:
            return 'We haven\'t implemented this maze pattern yet'
        return new_pattern.createMazeWall()
