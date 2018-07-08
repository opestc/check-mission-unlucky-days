def supply_line(you, depots, enemies):
        all_enemies=[]
        all_steps=[]
        for enemy in enemies:
            all_enemies+=adjacents(enemy)
            all_enemies.append(enemy)   
        depots=[depot for depot in depots if depot not in all_enemies]
        if not depots:
            return None
        else:
            for depot in depots:
                steps=1
                previous,path=[],[]
                start=you
                while start not in adjacents(depot):                    
                    previous.append(start)

                    print('previous steps',previous) #Mark all the chosed paths
                    steps+=1
                    
                    print('steps',steps) # Record the number of steps, initiated with 1
                    forwards=adjacents(start)
                    forwards=[step for step in forwards if (step not in all_enemies) and (step not in previous)]
                    print('forwards',forwards) #the next optional directions
                    
                    if forwards==[]:
                        if start==you:
                            steps=0
                            break
                        else:
                            start=path[-1]
                            path.pop()
                            steps-=2
                            continue
                    
                    for i in range(len(path)-1):
                        if start in adjacents(path[i]):
                            steps-=(len(path)-1-i)
                            path=path[0:i+1]
                            break
                    if start not in path:
                        path.append(start)
                    print('one path',path) #Record the possible shortest path, ignore the last two steps
                    
                    if set(forwards) & set(adjacents(depot)):
                        break
                     
                    forwards_dic={x: abs(ord(x[0])-ord(depot[0]))+abs(int(x[1])-int(depot[1])) for x in forwards}
                    forwards_dic=[k for k in sorted(forwards_dic.items(),key=lambda x:x[1])]
                    start=forwards_dic[0][0]
                    if len(forwards_dic) > 1:
                        if forwards_dic[0][1] == forwards_dic[1][1]:
                            if forwards_dic[0][0][0]==depot[0] or forwards_dic[0][0][1]==depot[1]:
                                start=forwards_dic[1][0]
                            elif path[-1][0]==forwards_dic[0][0][0] and abs(ord(forwards_dic[1][0][0])-ord(depot[0]))>=2:
                                start=forwards_dic[1][0]
                    
                    print('Next step',start) #Next step
                print('total number of steps',steps)
                all_steps.append(steps) 
            print(all_steps)
            if all(all_steps)==0:
                return None
            return min(step for step in all_steps if step!=0)   

def adjacents(point):
            data=[] 
            data.append(point[0]+str(int(point[1])+1))
            data.append(point[0]+str(int(point[1])-1))
            data.append(chr(ord(point[0])-1)+point[1])
            data.append(chr(ord(point[0])+1)+point[1])
            if (ord(point[0])-ord('A'))%2:
                data.append(chr(ord(point[0])-1)+str(int(point[1])+1))
                data.append(chr(ord(point[0])+1)+str(int(point[1])+1))
            else:
                data.append(chr(ord(point[0])-1)+str(int(point[1])-1))
                data.append(chr(ord(point[0])+1)+str(int(point[1])-1))
        
            data=[x for x in data if x[0]  in 'ABCDEFGHIJKL' and x[1] in '123456789' and len(x)==2]
            return data

if __name__ == '__main__':
        assert supply_line("B4", {"F4"}, {"D4"}) == 6, 'simple'
        assert supply_line("A3", {"A9","F5", "G8"}, {"B3", "G6"}) == 11, 'multiple'
        assert supply_line("C2", {"B9", "F6"}, {"B7", "E8", "E5", "H6"}) is None, 'None'
        assert supply_line("E5", {"C2", "B7", "F8"}, set()) == 4, 'no enemies'
        assert supply_line("A5", {"A2", "B9"}, {"B3", "B7", "E3", "E7"}) == 13, '2 depots'
        
        print('"Run" is good. How is "Check"?')
