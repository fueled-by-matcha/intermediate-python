class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudents
  
  def setNumberOfStudents(self, number):
    self.numberOfStudents = number
  
  def __repr__(self):
    return "A {} school named {} with {} students.".format(self.level, self.name, self.numberOfStudents)

class PrimarySchool(School):
  def __init__(name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def getPickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    schoolRepr = super().__repr__()
    return schoolRepr + "The pickup policy is {}".format(self.pickupPolicy)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().init(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def getSportsTeams(self):
    return self.sportsTeams
  
  def setSportsTeams(self, sportsTeams):
    self.sportsTeams = sportsTeams
  
  def __repr__(self):
    schoolRepr = super().__repr__()
    return schoolRepr + "The sports teams are {}".format(self.sportsTeams)
