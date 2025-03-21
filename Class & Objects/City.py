class City:
  def __init__(self, name, country, population, landmarks):

    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

mn = City('Minneapolis', 'United States', 425115, 'Stone Arch Bridge')

print(vars(mn))

