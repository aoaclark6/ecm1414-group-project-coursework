'''
An event planner containing the implementation of events
and how they fit within a schedule
'''

class Event:
    '''
    A container representing an event
    how long it takes and an enjoyment value
    '''

    def __init__(self, title, time_taken, enjoyment_value):
        self.title = title
        self.time = time_taken
        self.enjoyment_value = enjoyment_value


class Schedule:
    '''
    A container for all SELECTED events, only
    allowing an event to be added if it fits
    within the constraints
    '''
    def __init__(self, max_time: int):
        self.max_time = max_time

        self.total_time = 0
        self.total_enjoyment = 0
        self.event_amount = 0

        self.events: list[Event]
        self.events = []


    def add_event(self, event: Event) -> None:
        '''
        Adds an event to the schedule
        '''
        if self.max_time - self.total_time >= event.time:
            self.events.append(event)
            self.event_amount += 1

            self.total_time += event.time
            self.total_enjoyment += event.enjoyment_value

        else:
            print(f"Event {event.title} could not be added to the schedule")

    def display_schedule(self) -> None:
        '''
        Displays the schedule and lists all events
        displays metrics about the schedule
        '''
        print("SCHEDULE:\n")
        print(f"Total events: {self.event_amount}")
        print(f"Total time: {self.total_time}")
        print(f"Total enjoyment: {self.total_enjoyment}\n")
        print("Events Selected:")
        for event in self.events:
            print(event.title)


if __name__ == "__main__":
    MAX_TIME = 12


    event_data = [
        # name, time, enjoyment
        ["Cooking", 1, 50],
        ["Walk", 2, 75],
        ["Bowling", 4, 175],
        ["Movies", 2, 100],
        ["Movie Marathon", 10, 10]
    ]

    event_list = []
    for event_datum in event_data:
        event_list.append(Event(
            title = event_datum[0],
            time_taken = event_datum[1],
            enjoyment_value = event_datum[2]))

    schedule = Schedule(MAX_TIME)
    schedule.add_event(event_list[0])
    schedule.add_event(event_list[-1])
    # schedule.add_event(event_list[1]) # Will cause an error for not enough time
    schedule.display_schedule()
