//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        function goGameCanvas(dom, input) {
            const difference = (a1, a2)=>a1.filter(v => ! a2.includes(v));
            const intersection = (a1, a2)=>a1.filter(v => a2.includes(v));
            const union=(a1, a2)=>a1.concat(a2.filter(v=>!a1.includes(v)));
            const clone = a1 => a1.concat([]);

            function go_game(board) {

                const [width, height] = [board[0].length, board.length];

                const safe = (point, stone)=>{
                    const enemy = stone === 'W'? 'B': 'W';
                    const [y, x] = [Math.floor(point/10), point % 10];
                    let result = [];

                    [[y-1, x], [y, x+1], [y+1, x], [y, x-1]].forEach(yx=>{
                        const [ty, tx] = yx;
                        if (0 <= ty && ty < height
                            && 0 <= tx && tx < width) {
                            if (board[ty][tx] === '+') {
                                result.push(board[ty][tx]);
                            } else {
                                if (board[ty][tx] != enemy)
                                    result.push(ty*10+tx);
                            }
                        }
                    });
                    return result;
                };

                const search = (y, x, stone) => {

                    let done_cells = [y*10+x];
                    let next_cells = [y*10+x];

                    while (next_cells.length) {
                        const search_cells = next_cells;
                        next_cells = [];

                        for (let i=0; i < search_cells.length; i += 1) {
                            const safe_cells = safe(search_cells[i], stone);
                            if (safe_cells.includes('+')) {
                                return true
                            }
                            next_cells = union(next_cells, safe_cells);
                        }
                        next_cells = difference(next_cells, done_cells);
                        done_cells = union(done_cells, next_cells);
                    };
                    return false
                };

                const result = {'B': [], 'W': []};
                board.forEach((row, y)=>{
                    row.split('').forEach((stone, x)=>{
                        if (stone !== '+' && ! search(y, x, stone)) {
                            result[stone].push(y*10+x);
                        }
                    });
                });
                return result;
            }

            const attr = {
                rect: {
                    go: {
                        'stroke': 'orange',
                        'stroke-width': 3,
                    }
                },
                stone: {
                    W: {
                        'fill': 'white',
                        'stroke': '#294270',
                        'stroke-width': 1,
                    },
                    B: {
                        'fill': '#294270',
                        'stroke': '#294270',
                        'stroke-width': 1,

                    },
                },
                eaten: {
                    W: {
                        'stroke': 'orange',
                        'fill': 'orange',
                        'font-size': 16,
                        'font-weight': 100,
                        'font-family': 'helvetica',
                    },
                    B: {
                        'stroke': 'orange',
                        'fill': 'orange',
                        'font-size': 16,
                        'font-weight': 100,
                        'font-family': 'helvetica',
                    },
                }
            };
            const [w, h] = [input[0].length, input.length];
            const SIZE = 20; 
            const paper = Raphael(dom, w*SIZE, h*SIZE, 0, 0);
            const os = SIZE/2;
            const answer = go_game(input); 

            // draw board
            for (let i=0; i < h-1; i += 1){
                for (let j=0; j < w-1; j += 1){
                    paper.rect(
                        SIZE*i+os,
                        SIZE*j+os,
                        SIZE, SIZE).attr(attr.rect.go);
                }
            }
            // set stone
            input.forEach((row, i)=>{
                row.split('').forEach((s,j)=>{
                    if (s !== '+'){
                        paper.circle(
                            j*SIZE+os,
                            i*SIZE+os,
                            SIZE/2-1).attr(attr.stone[s]);
                    }
                });
            });
            // set number
            answer.W.forEach((point, i)=> {
                paper.text( 
                    (point%10)*SIZE+os, 
                    Math.floor(point/10)*SIZE+os+1, i+1).attr(
                        attr.eaten.W);
            });
            answer.B.forEach((point, i)=> {
                paper.text( 
                    (point%10)*SIZE+os, 
                    Math.floor(point/10)*SIZE+os+1, i+1).attr(
                        attr.eaten.B);
            });
        }
        
        var $tryit;
        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'go_game',
                js: 'goGame'
            },
            animation: function($expl, data){
                goGameCanvas(
                    $expl[0],
                    data.in
                );
            }
        });
        io.start();
    }
);
