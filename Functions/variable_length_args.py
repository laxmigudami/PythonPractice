def var_args(**kwargs): #variable length keyward args
  print(kwargs)
var_args(website = "FACEPrep", article = "Python", days = 60)


def var_args(*args): #variable-length positionale args
  print(args)
var_args("FACEPrep", "Python", 30, 29.56)