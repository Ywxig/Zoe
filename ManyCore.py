class Rooport():

    def Filter(Name, Filter):
        Fail = open(str(Name), 'r')
        Text = Fail.read()
        Tl = Text.split(str(Filter))

        Author = Tl[0]
        Log = Tl[1]

        Fail.close    

    def Creat(Name):
        Fail = open(str(Name), 'w')
        Fail.write()
        Fail.close

    def Read(Name):
        Fail = open(str(Name), 'r')
        Text = Fail.read()
        return Text

    def Write(Name, Author, Wal, Many, Log):
        Fail = open(str(Name), 'a')
        Fail.write('\n' + str(Author) + str(Wal) + str(Log) + str(Wal) + str(Many) )
        Fail.close