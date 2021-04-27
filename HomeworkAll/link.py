import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()


#Center
G.add_edge('Sara Buri',"Nakorn Nayok",weight=58)
G.add_edge("Sara Buri",'Prathum Thani',weight=85)
G.add_edge('Prathum Thani',"Non Buri",weight=27)
G.add_edge('Prathum Thani',"Bankok",weight=42)
G.add_edge('Prathum thani',"Nakorn Nayok",weight=117)
G.add_edge('Nakorn Nayok',"Prachin Buri",weight=20)
G.add_edge('Nakorn Nayok',"Chacherngsau",weight=75)
G.add_edge('Prachin Buri',"Bankok",weight=145)
G.add_edge('Prachin Buri',"Chacherngsau",weight=74)
G.add_edge('Prachin Buri',"Sakiaw",weight=104)
G.add_edge('Non Buri',"Bankok",weight=22)
G.add_edge('Bankok',"Chacherngsau",weight=85)
G.add_edge('Bankok',"Samut Prakarn",weight=26)
G.add_edge('Samut Prakarn',"Chon Buri",weight=70)
G.add_edge('Chon Buri',"Chacherngsau",weight=50)
G.add_edge('Chon Buri',"Rayong",weight=98)
G.add_edge('Rayong',"Chacherngsau",weight=135)
G.add_edge('Rayong',"Chantha Buri",weight=111)
G.add_edge('Chantha Buri',"Chacherngsau",weight=206)
G.add_edge('Chatha Buri',"Sakiaw",weight=161)
G.add_edge('Chatha Buri',"Trat",weight=69)
G.add_edge('Chacherngsau',"Sakiaw",weight=130)
#South
G.add_edge('Prajuab Kereekun',"Chumpon",weight=189)
G.add_edge('Chumpon',"Ranong",weight=126)
G.add_edge('Ranong',"Suras Thani",weight=218)
G.add_edge('Suras Thani',"Chumpon",weight=184)
G.add_edge('Chumpon',"Panga",weight=231)
G.add_edge('Panga',"Phuket",weight=87)
G.add_edge('Panga',"Suras Thani",weight=159)
G.add_edge('Suras Thani',"Krabi",weight=156)
G.add_edge('Krabi',"Panga",weight=74)
G.add_edge('Krabi',"Nakornsrithummaras",weight=172)
G.add_edge('Nakornsrithummaras',"Suras Thani",weight=140)
G.add_edge('Nakornsrithummaras',"Trang",weight=131)
G.add_edge('Trang',"Krabi",weight=126)
G.add_edge('Trang',"Pathalung",weight=75)
G.add_edge('Pathalung"',"Nakornsrithummaras",weight=109)
G.add_edge('Prajuab Kereekun',"Chon Buri",weight=75)
#North
G.add_edge('Sara Buri',"Nakorn Sawan",weight=75)
G.add_edge('Nakorn Sawan',"Uthai Thani",weight=43)
G.add_edge('Nakorn Sawan',"Khumpangpet",weight=132)
G.add_edge('Khumpangpet',"Pijit",weight=100)
G.add_edge('Pijit',"Nakorn Sawan",weight=104)
G.add_edge('Nakorn Sawan',"Petchabun",weight=174)
G.add_edge('Petchabun',"Pijit",weight=133)
G.add_edge('Pijit',"Pisanulok",weight=57)
G.add_edge('Pisanulok',"Khumpangpet",weight=110)
G.add_edge('Pisanulok',"Udaradit",weight=108)
G.add_edge('Udaradit',"Sukothai",weight=91)
G.add_edge('Sukothai',"'Pisanulok",weight=58)
G.add_edge('Sukothai',"Khumpangpet",weight=71)
G.add_edge('Khumpangpet',"Tak",weight=62)
G.add_edge('Tak',"Sukothai",weight=85)
G.add_edge('Tak',"Maehongsorn",weight=508)
G.add_edge('Maehongsorn',"Chaingmai",weight=237)
G.add_edge('Chaingmai',"Lumphun",weight=21)
G.add_edge('Lumphun',"Tak",weight=241)
G.add_edge('Lumphun',"Lumpang",weight=114)
G.add_edge('Lumpang',"Tak",weight=188)
G.add_edge('Lumpang',"Sukothai",weight=195)
G.add_edge('Lumpang',"Prae",weight=96)
G.add_edge('Prae',"Sukothai",weight=163)
G.add_edge('Prae',"Udaradit",weight=72)
G.add_edge('Prae',"Nahn",weight=119)
G.add_edge('Nahn',"Payauh",weight=148)
G.add_edge('Payauh',"Prae",weight=143)
G.add_edge('Payauh',"Lumpang",weight=142)
G.add_edge('Chaingrai',"Payauh",weight=92)
G.add_edge('Chaingrai',"Lumpang",weight=229)
G.add_edge('Chaingrai',"Chaingmai",weight=190)
G.add_edge('Petchabun',"Chaiyaphum",weight=75)
#East-North
G.add_edge('Chaiyaphum',"Nakornsrithummaras",weight=121)
G.add_edge('Chaiyaphum',"Korngaen",weight=140)
G.add_edge('Korngaen',"Nakornsrithummaras",weight=192)
G.add_edge('Nakornsrithummaras',"Mahasarakahm",weight=214)
G.add_edge('Mahasarakahm',"Korngaen",weight=72)
G.add_edge('Mahasarakahm',"Buriram",weight=149)
G.add_edge('Buriram',"Roied",weight=149)
G.add_edge('Roied',"Mahasarakahm",weight=44)
G.add_edge('Roied',"Surin",weight=149)
G.add_edge('Surin',"Buriram",weight=55)
G.add_edge('Buriram',"Nakornrachasrima",weight=127)
G.add_edge('Nakornrachasrima',"Chaiyaphum",weight=121)
G.add_edge('Surin',"Srisaket",weight=105)
G.add_edge('Srisaket',"Roied",weight=146)
G.add_edge('Srisaket',"Yasotorn",weight=103)
G.add_edge('Yasotorn',"Roied",weight=68)
G.add_edge('Yasotorn',"Ubonracha thani",weight=103)
G.add_edge('Ubonracha thani',"Srisaket",weight=65)
G.add_edge('Ubonracha thani',"Amnacharurn",weight=27)
G.add_edge('Amnacharurn',"Mukdahan",weight=99)
G.add_edge('Mukdahan',"Yasotorn",weight=115)
G.add_edge('Yasotorn',"Amnacharurn",weight=77)
G.add_edge('Mukdahan',"Roied",weight=149)
G.add_edge('Roied',"Kalasin",weight=49)
G.add_edge('Kalasin',"Mukdahan",weight=164)
G.add_edge('Kalasin',"'Mahasarakahm",weight=48)
G.add_edge('Kalasin',"Korngaen",weight=77)
G.add_edge('Korngaen',"Mahasarakahm",weight=72)
G.add_edge('Korngaen',"Nongbualampuu",weight=75)
G.add_edge('Nongbualampuu',"Leuy",weight=99)
G.add_edge('Leuy',"Korngaen",weight=207)
G.add_edge('Leuy',"Chaiyaphum",weight=227)
G.add_edge('Leuy',"Nongkai",weight=234)
G.add_edge('Nongkai',"Udon Thani",weight=52)
G.add_edge('Udon Thani',"Nongbualampuu",weight=51)
G.add_edge('Udon Thani',"Korngaen",weight=121)
G.add_edge('Udon Thani',"Kalasin",weight=147)
G.add_edge('Kalasin',"Sakonakorn",weight=129)
G.add_edge('Sakonakorn',"Udon Thani",weight=186)
G.add_edge('Sakonakorn',"Mukdahan",weight=114)
G.add_edge('Mukdahan',"Nakornpanom",weight=110)
G.add_edge('Nakornpanom',"Sakonakorn",weight=94)
G.add_edge('Sakonakorn',"Buengkarn",weight=195)
G.add_edge('Buengkarn',"Sakonakorn",weight=181)
G.add_edge('Buengkarn',"Udon Thani",weight=207)
G.add_edge('Udon Thani',"Nongkai",weight=52)
G.add_edge('Nongkai',"Buengkarn",weight=135)

try:
    again = 'y'
    while again.lower() == 'y': 
        print('1.No visit')
        print('2. 1 visit')
        print('3. 2 visit')
        print('4.Exit')
        key = int(input("Enter the Number:"))
        if key == 1:
            Province_start = input('Province Start: ')
            Province_end = input('Province End: ')
            all_paths = list(nx.shortest_simple_paths(G,source=Province_start,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1],'Km')

            print('Province to pass through shortest path Second is :',three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1],'Km')

            print('Province to pass through shortest path Third is :',three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1],'Km')
        if key == 2:
            Province_start = input('Province Start: ')
            Province_stay_1 = input('Province stay: ')
            Province_end = input('Province End: ')
            path_length = nx.shortest_path_length(G,source=Province_start,target=Province_stay_1,weight='weight')
            shortest_path = list(nx.shortest_path(G,source=Province_start,target=Province_stay_1,weight='weight'))
            
            all_paths = list(nx.shortest_simple_paths(G,source=Province_stay_1,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',shortest_path[:-1]+three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1]+path_length,'Km')

            print('Province to pass through shortest path Second is :',shortest_path[:-1]+three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1]+path_length,'Km')

            print('Province to pass through shortest path Third is :',shortest_path[:-1]+three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1]+path_length,'Km')
        if key == 3:
            Province_start = input('Province Start: ')
            Province_stay_1 = input('Province stay 1: ')
            Province_stay_2 = input('Province stay 2: ')
            Province_end = input('Province End: ')
            path_length1 = nx.shortest_path_length(G,source=Province_start,target=Province_stay_1,weight='weight')
            shortest_path1 = list(nx.shortest_path(G,source=Province_start,target=Province_stay_1,weight='weight'))

            path_length2 = nx.shortest_path_length(G,source=Province_stay_1,target=Province_stay_2,weight='weight')
            shortest_path2 = list(nx.shortest_path(G,source=Province_stay_1,target=Province_stay_2,weight='weight'))
            
            all_paths = list(nx.shortest_simple_paths(G,source=Province_stay_2,target=Province_end,weight=None))
            o = []
            p = []
            m = 0
            three_shortest_path = []
            for x,i in enumerate(all_paths):
                    
                for k in range(len(i)):
                    if k != len(i)-1:
                        o.append(nx.shortest_path_length(G,source=i[k],target=i[k+1],weight='weight'))
                all_paths[x].append(sum(o))
                o = []
            for y in all_paths:
                for t in y:
                    if type(t) == int:
                        p.append(t)
            while m != 3:
                three_shortest_path.append(all_paths[p.index(min(p))])
                k = p.index(min(p))
                p.pop(k)
                all_paths.pop(k)
                m +=1
            print('Province to pass through shortest path First is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[0][:-1] )
            print('Distance shortest path First from',Province_start,'to',Province_end,'is:' , three_shortest_path[0][-1]+path_length1+path_length2,'Km')

            print('Province to pass through shortest path Second is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[1][:-1] )
            print('Distance shortest path Second from',Province_start,'to',Province_end,'is:' , three_shortest_path[1][-1]+path_length1+path_length2,'Km')

            print('Province to pass through shortest path Third is :',shortest_path1[:-1]+shortest_path2[:-1]+three_shortest_path[2][:-1] )
            print('Distance shortest path Third from',Province_start,'to',Province_end,'is:' , three_shortest_path[2][-1]+path_length1+path_length2,'Km')
        if key == 4:
            break
        else:
            again = 'y'
        edge_labels = nx.get_edge_attributes(G,'weight')
        pos = nx.spring_layout(G)
        nx.draw(G,pos ,with_labels=True,font_color="black",font_size="5",node_size= 2000)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
        again = input('Enter y to do again or n it exit: ')
except:
    print('End')
