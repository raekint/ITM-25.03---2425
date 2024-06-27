'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph and to_member in social_graph:
        following_fm = social_graph[from_member].get("following")
        following_tm = social_graph[to_member].get("following")
        if following_fm == []:
            if from_member in following_tm:
                return("followed by")
            return("no relationship")
        elif following_tm ==[]:
            if to_member in following_fm:
                    return("follower")
            return("no relationship")
        elif from_member in following_tm:
            if to_member in following_fm:
                return("friends")
            return("followed by")
        elif to_member in following_fm:
            return("follower")
        else: return("no relationship")
    else: return("no relationship")


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    n = len(board)
    if n == 0:
        return 'NO WINNER'

    for row in board:
        if all(cell == row[0] and cell != '' for cell in row):
            return row[0]

    for col in range(n):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(n)):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(n)):
        return board[0][0]

    if all(board[i][n - 1 - i] == board[0][n - 1] and board[i][n - 1 - i] != '' for i in range(n)):
        return board[0][n - 1]

    for row in board:
        if '' in row:
            return 'NO WINNER'

    return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    stops = list(route_map.keys())

    for n in stops:
        if first_stop == n[0]:
            start = n
        if second_stop == n[1]:
            end = n
    start_index = stops.index(start)
    end_index = stops.index(end)


    total__time = 0
    if start_index <= end_index:
        for i in range(start_index, end_index+1):
            ttm = route_map[stops[i]]
            time = ttm["travel_time_mins"]
            total__time = total__time + time
    elif start_index > end_index:
        for i in range(start_index, len(route_map)):
            ttm = route_map[stops[i]]
            time = ttm["travel_time_mins"]
            total__time = total__time + time
        for i in range(0, end_index+1):
            ttm = route_map[stops[i]]
            time = ttm["travel_time_mins"]
            total__time = total__time + time

    return(total__time)