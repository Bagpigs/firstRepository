#stage2

#input height, amount
#output throws
height = 456

#test all percentages
#for every percentage whats the maximal throws =: max?  -> get best percentage

percentage_list = [[i,0] for i in range(101)]
print(percentage_list)
for percentage in range(1,101):
    for k in range(height+1):
        pos_worker = -1
        steps_upwards = 0
        while pos_worker < k:
            steps_upwards += 1
            last_pos_worker = pos_worker
            meters_left = height - pos_worker
            distance = max(1,round(meters_left*percentage*0.01))
            pos_worker = pos_worker + distance
        steps_upwards += k - last_pos_worker
        if pos_worker == k:
            steps_upwards -= 1
        if steps_upwards > percentage_list[percentage][1]:
            percentage_list[percentage][1] = steps_upwards
            #percentage_list[percentage][2] = k

percentage_list = percentage_list[1:101]

print(percentage_list)






#runnig_rec_func()
