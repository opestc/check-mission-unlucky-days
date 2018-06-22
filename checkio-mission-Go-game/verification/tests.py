"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['++++W++++',
                      '+++WBW+++',
                      '++BWBBW++',
                      '+W++WWB++',
                      '+W++B+B++',
                      '+W+BWBWB+',
                      '++++BWB++',
                      '+B++BWB++',
                      '+++++B+++'],
            "answer": {'B': 3, 'W': 4}
        },
        {
            "input": ['+++++++++',
                      '++++BW+++',
                      '+BWWBBW++',
                      'BWB+WWB++',
                      'BWB+W+B++',
                      'BWBBWWWB+',
                      '+B++BWB++',
                      '+B++BWB++',
                      '++++WBW++'],
            "answer": {'B': 1, 'W': 3}
        }
    ],
    "Extra": [
        {
            "input": ['+++++++++',
                      '+++W+W+++',
                      '++BW++W++',
                      '+B+++WWW+',
                      'BWB++WBBW',
                      '+B+B+WBBW',
                      '++++++WW+',
                      '+B+++++++',
                      '+++++++++'],
            "answer": {'B': 4, 'W': 1}
        },
        {
            "input": ['++++W++++',
                      '+++++W+++',
                      '+++++BW++',
                      '++++WWB++',
                      '++++B++++',
                      '++++WBWB+',
                      '+B+++WBW+',
                      'BWB++WBW+',
                      'WB+++BW++'],
            "answer": {'B': 2, 'W': 2}
        },
	{
            "input": ['++++W++++',
                      '++++BW+++',
                      '++B+BBW++',
                      '+W++WWB++',
                      '+W++B+B++',
                      '+W+BW+WB+',
                      '+++++WB++',
                      '+B++BWB++',
                      '+++++B+++'],
            "answer": {'B': 0, 'W': 0}
        },
        {
            "input": ['++++W++++',
                      '++++WW+++',
                      '++B+WBW++',
                      '+W++WWB++',
                      '+W++B+B++',
                      '+W+BW+WB+',
                      '+++++BB++',
                      '+B++BWB++',
                      '+++++B+++'],
            "answer": {'B': 1, 'W': 1}
        },
        {
            "input": ['+++++++++',
                      '++WWWW+++',
                      '+WBBBBW++',
                      '+WBBBBW++',
                      '+WBBBBW++',
                      '+WBBBBWB+',
                      '++WWWW+++',
                      '+B++BWB++',
                      '+++++B+++'],
            "answer": {'B': 16, 'W': 0}
        },
	{
            "input": ['+++WW++++',
                      '++WBBW+++',
                      '++BWBBW++',
                      '+W++WWB++',
                      '+W++BBB++',
                      '+W+BWWWB+',
                      '++++BWB++',
                      '+B++BWB++',
                      '+++++B+++'],
            "answer": {'B': 4, 'W': 5}
        },
        {
            "input": ['+++BWB+++',
                      '++++BW+++',
                      '++B+BBW++',
                      '+W++WWB++',
                      '+W++B+B++',
                      '+++++++++',
                      '++BBBB+++',
                      '+BWWWWB++',
                      '++BBBB+++'],
            "answer": {'B': 0, 'W': 5}
        },
        {
            "input": ['++++BB+++',
                      '++++BWB++',
                      '++B+BBWB+',
                      '+W++WWB++',
                      '+W++B+B++',
                      '+W+B+++B+',
                      '+++++WB++',
                      '+B++BWB++',
                      '++++WBW++'],
            "answer": {'B': 1, 'W': 2}
        },
        {
            "input": ['BW+++++',
                      'W++W+W+',
                      '+++W++W',
                      '+B+++WW',
                      'B++++++',
                      '+B+B++B',
                      '+++++BW'],
            "answer": {'B': 1, 'W': 1}
        },
        {
            "input": ['+W+++++',
                      'WBWW+WB',
                      '+WBW+BW',
                      '+BBBBWW',
                      'BWWWWWB',
                      '+BBBBBB',
                      '++++++W'],
            "answer": {'B': 1, 'W': 8}
        },
	{
            "input": ['+++++++',
                      '+++W+W+',
                      '++BW++W',
                      '+B+++WW',
                      'BWB++WB',
                      '+B+B+WB',
                      '++++++W'],
            "answer": {'B': 2, 'W': 1}
        },
        {
            "input": ['+++++',
                      '++W++',
                      '+WBW+',
                      'WBBBW',
                      '+WWW+'],
            "answer": {'B': 4, 'W': 0}
        },
        {
            "input": ['+++++',
                      '+++W+',
                      '++BW+',
                      '+B+++',
                      '+++++'],
            "answer": {'B': 0, 'W': 0}
        },
        {
            "input": ['+++B+',
                      '++BWB',
                      '+WBWB',
                      'WBWB+',
                      '+W+++'],
            "answer": {'B': 1, 'W': 2}
        }
    ]
}
