#
# DisplayClass.py - Thread safe class to handle the Daisy-24 LCD display module for the TERRA board
#



import ablib # by Acme Systems srl

import logging
import threading






class Display( object, ablib.Daisy24 ):

  """
  Class inherited from AbLib.Daisy24

  Usage:

  # in your main program initialize the logging facility
  logging.basicConfig( level = logging.DEBUG, format = '(%(threadName)-10s) %(message)s', )

  # create a Display instance
  Lcd = Display()
  time.sleep( 5 ) # for display purpose

  From this moment forward, you can call the specific class thread safe method
  Lcd.PutStrings()
  and all the base class methods as well
  Lcd.pressed()
  Lcd.setcontrast()
  ...

  """

  # constructor
  def __init__( self ):
    ClassName = self.__class__.__name__
    logging.debug( "%s === Constructor called ===" % ( ClassName ) )

    ablib.Daisy24.__init__( self )
    ablib.Daisy24.backlighton( self )
    ablib.Daisy24.clear( self )
    ablib.Daisy24.setcurpos( self, 0, 0 )
    ablib.Daisy24.putstring( self, "Hello           " )
    ablib.Daisy24.setcurpos( self, 0, 1 )
    ablib.Daisy24.putstring( self, "world!          " )

    self.__Lock = threading.Lock() # private attribute
    return

  def PutStrings( self, Row1 = "Demo1", Row2 = "Demo2" ):
    logging.debug( "Waiting for lock" )
    self.__Lock.acquire()
    try:
      logging.debug( "Acquired lock" )

      ablib.Daisy24.clear( self )
      ablib.Daisy24.setcurpos( self, 0, 0 )
      ablib.Daisy24.putstring( self, Row1 )
      ablib.Daisy24.setcurpos( self, 0, 1 )
      ablib.Daisy24.putstring( self, Row2 )

    finally:
      self.__Lock.release()
    return

  # destructor
  def __del__( self ):
    ClassName = self.__class__.__name__
    logging.debug( "%s === Destructor called ===" % ( ClassName ) )

    ablib.Daisy24.clear( self )
    ablib.Daisy24.setcurpos( self, 0, 0 )
    ablib.Daisy24.putstring( self, "      BYE       " )
    ablib.Daisy24.setcurpos( self, 0, 1 )
    ablib.Daisy24.putstring( self, "       BYE      " )
    ablib.Daisy24.backlightoff( self )

    return



# EOF
