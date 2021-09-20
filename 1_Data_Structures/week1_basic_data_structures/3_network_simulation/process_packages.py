# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque(maxlen = size)
    
    def popper(self,request):
        response = []
        if  len(self.finish_time)!=0:
            while len(self.finish_time)!=0 and self.finish_time[0].time_to_process <= request.arrived_at:
                response.append(Response(False, self.finish_time.popleft().arrived_at))
        return response


        
    def process(self, request = Request(0,0),cl = False):
        if(cl):
            response = Response(False, self.finish_time.popleft().arrived_at)
            return response
        # When a new packet arrives, you will first need to pop from the front of finish_time all the packets which are already 
        # processed by the time new packet arrives.

        if  len(self.finish_time)!=0:
           if len(self.finish_time)!=0 and self.finish_time[0].time_to_process <= request.arrived_at:
               return Response(False, self.finish_time.popleft().arrived_at)
        # Then you try to add the finish time for the new packet in finish_time.
        # If the buffer is full (there are already S finish times in finish_time), the packet is dropped.
        if len(self.finish_time) == self.size: # calculated the length of my deque for each request using len() function
            return Response(True, -1)
        else: 
            #Otherwise, its processing finish time is added to finish_time.
            if len(self.finish_time)==0:
                self.finish_time.append(request)
                
            else:
                #Otherwise, computer will start processing the new packet as soon as it
                #finishes to process the last of the packets currently in finish_time (here is when you need to access the
                #last element of finish_time to determine when the computer will start to process the new packet).
                # You will also need to compute the processing finish time by adding Pi to the processing start time 
                # and push it to theback of finish_time.
                request.time_to_process += self.finish_time[-1].time_to_process
                self.finish_time.append(request)
        
        ###WARN ### 
        # You need to remember to output the processing start time for each packet instead of the processing finish 
        # time which you store in finish_time.

        

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        response = buffer.process(request) 
        if(response):
            responses.append(response)
        
    while len(buffer.finish_time) != 0:
        responses.append(buffer.process(cl = True))
        
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
