class Journal:
  def __init__(self):
    self.entries = []
    self.count = 0

  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')

  def remove_entry(self, pos):
    del self.entries[pos]

  def __str__(self):
    return '\n'.join(self.entries)

  def save(self, filename):
    # Breaking SRP
    pass

  def load(self, filename):
    # Breaking SRP
    pass

  def low_from_web(self, uri):
    # Breaking SRP
    pass


class PersistenceManager:
  @staticmethod
  def save_to_file(journal, filename):
    with open(filename, 'w') as file:
      file.write(str(journal))


my_journal = Journal()
my_journal.add_entry('I ate breakfast')
my_journal.add_entry('I slept a lot')
print(f'Journal Entries:\n{my_journal}')

journal_file = r'/tmp/journal_tmp.txt'
PersistenceManager.save_to_file(my_journal, journal_file)

with open(journal_file) as file_handle:
  print('reading from filename')
  print(file_handle.read())
