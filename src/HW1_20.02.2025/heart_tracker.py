storage_data = {}

def accept_package(time, heart_rate):
    storage_data[time] = heart_rate
    print(check_correct_data(time, heart_rate))
    print(message(time, heart_rate))
    print('')
    print(motivation_message(heart_rate))
    return storage_data

def check_correct_data(time, heart_rate):
  last_time = max(storage_data.keys())
  if not (isinstance(time, str) and isinstance(heart_rate, int)):
    return False
  if time <= last_time:
    return False
  elif not time or heart_rate is None:
    return False
  else:
    return True

def message(time, heart_rate):
    return f'Время: {time}. \n Частота сердечных сокращений за сегодня: {heart_rate}. \n Нормальная активность! Продолжайте движения'

def motivation_message(heart_rate):
  if heart_rate < 60:
    return f'Главное — быть активным!'
  elif 60 <= heart_rate < 80:
      return f'Хороший результат, Вы движетесь в правильном направлении!'
  elif 80 <= heart_rate < 100:
      return f'Осторожно, успокойтесь!'
  elif heart_rate >= 100:
      return f'Осторожно, что-то не так! Обратитесь к врачу.'
  else:
      return f'Введите корректные данные про интенсивность сердечного ритма!'

if __name__ == '__main__':
    accept_package("12:00", 65)
    accept_package("10:00", 75)