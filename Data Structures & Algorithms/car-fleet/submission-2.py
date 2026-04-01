class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i])) 
        
        cars = sorted(cars, key=lambda x: x[0], reverse=True) 

        stack.append(cars[0])
        for i in range(1, len(cars)): 
            car = cars[i]
            p, s = car[0], car[1]
            d = target - p
            t = d/s 


            recent = stack[-1]
            sp, ss = recent[0], recent[1] 
            sd = target - sp 
            st = sd / ss 

            if st < t: 
                stack.append(car)
                

        
        return len(stack)



        
            
        