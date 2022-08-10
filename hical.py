"""
Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.
"""

def merge_ranges(arr):
    for i in range(len(arr) - 2):
        for j in range(len(arr) - (i+1)):
            if arr[j][0] > arr[j+1][0]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    condensed = []
    i = 0
    while i < len(arr) - 1:
        if arr[i][1] >= arr[i+1][0]:
            if arr[i][1] >= arr[i+1][1]:
                condensed.append((arr[i][0], arr[i][1]))
                i += 2
            else:
                condensed.append((arr[i][0], arr[i+1][1]))
                i += 2
        else:
            condensed.append((arr[i][0], arr[i][1]))
            i += 1
    return condensed

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))


# ideal solution
"""
  def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
"""
