class ColorPrint:
  
  BLACK = 30
  RED = 31
  GREEN = 32
  YELLOW = 33
  BLUE = 34
  MAGENTA = 35
  CYAN = 36
  WHITE = 37

  @staticmethod
  def log(msg: str, color=37, separator = '$$'):
    tmp = msg.split(separator)
    print(f'{tmp[0]}\x1b[{color}m{tmp[1]}\x1b[0m{tmp[2]}')

  @staticmethod
  def green(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.GREEN)

  @staticmethod
  def red(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.RED)

  @staticmethod
  def blue(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.BLUE)

  @staticmethod
  def yellow(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.YELLOW)
  
  @staticmethod
  def info(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.WHITE)
  
  @staticmethod
  def success(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.GREEN)
  
  @staticmethod
  def warn(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.YELLOW)
    
  @staticmethod
  def error(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.RED)
  
  @staticmethod
  def panic(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.MAGENTA)
    
  @staticmethod
  def cyan(msg: str):
    ColorPrint.log(f'$${msg}$$', ColorPrint.CYAN)
    
