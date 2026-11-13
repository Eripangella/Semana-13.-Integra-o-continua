class Aluno:
  def __init__(self, nome, sobrenome, nota):
    self.nome = nome;
    self.sobrenome = nome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);
