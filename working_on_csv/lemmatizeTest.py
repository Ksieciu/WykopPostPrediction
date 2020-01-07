from stringFunctions import lemmatize_words


test_string = "Nikt już nie dba o filmy Nikt nie chodzi już do kina ani nie ogląda telewizji kablowej Wszyscy oglądają wyłącznie Netflix To wydarzenie powinno wyglądać tak że wychodzę na środek tylko po to by powiedzieć Dobra robota Netflix Wygrałeś wszystko Dobranoc Ale nie musimy to przeciągać przez trzy godziny Moglibyśmy w tym czasie obejrzeć cały pierwszy sezon After Life zamiast tego wydarzenia Serial ten opowiada o mężczyźnie który chce się zabić bo jego żona umarła na raka a nadal jest o wiele zabawniejszy od tego Uwaga spoiler drugi sezon jest już w drodze więc ostatecznie nie zabił się Zupełnie jak Jeffrey Epstein przyp tłum amerykański multimilioner skazany na  lat więzienia za przestępstwa seksualne miał oferować wielu milionerom dziesiątki nieletnich w celu wykorzystania ich seksualnie wyrok został zmniejszony z dożywocia na skutek ugody według oficjalnej wersji popełnił samobójstwo w areszcie przed wydaniem swoich klientów Zamknijcie się Wiem że był waszym przyjacielem"

words_list = test_string.split()

lemmatized = lemmatize_words(words_list)

print(lemmatized)
