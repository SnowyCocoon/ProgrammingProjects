// import the robotjs library
var robot = require('robotjs');

function main() {
    console.log("Starting the bot... You have 4 seconds to open your client!");
    sleep(4000);
    console.log("Bot is running!");

    while (true) {
        var tree = findTree();
        if (tree == false) {
            rotateCamera();
            continue;
        }

        robot.moveMouseSmooth(tree.x, tree.y,1);
        sleep(500);
        robot.mouseClick();
        sleep(3000);
        dropLogs();
    }
}

function dropLogs() {
    var inventory_x = 1755;
    var inventory_y = 762;
    var log_color = "6d5432";

    var pixel_color = robot.getPixelColor(inventory_x,inventory_y);
    

    var wait_cycle = 0;
    var max_wait_cycle = 9;
    while(pixel_color != log_color && wait_cycle < max_wait_cycle){
        sleep(1000)
        var pixel_color = robot.getPixelColor(inventory_x,inventory_y);
        wait_cycle++;
    }

    if(robot.getPixelColor(inventory_x,inventory_y) == log_color){
        robot.moveMouseSmooth(inventory_x, inventory_y,1);
        sleep(100);
        robot.keyToggle('shift', 'down');
        sleep(10);
        robot.mouseClick();
        sleep(10);
        robot.keyToggle('shift', 'up');
        sleep(1000);
    }
}

function findTree() {
    var x = 300, y = 300, width = 1300, height = 400;
    var img = robot.screen.capture(x, y, width, height);

    var tree_colors = ["5b462a", "60492c", "6a5130", "705634", "6d5432", "574328"];

    for (var i = 0; i < 500; i++) {
        var random_x = getRandomInt(0, width-1);
        var random_y = getRandomInt(0, height-1);
        var sample_color = img.colorAt(random_x, random_y);

        if (tree_colors.includes(sample_color)) {
            var screen_x = random_x + x;
            var screen_y = random_y + y;


            if(confirmTree(screen_x,screen_y)){
                console.log("Found a tree at: " + screen_x + ", " + screen_y + " color " + sample_color);
                return {x: screen_x, y: screen_y};
            } else {
                console.log("unconfirmed tree");
            }
            
        }
    }
    
    return false;
}

function rotateCamera() {
    console.log("Rotating camera");
    robot.keyToggle('right', 'down');
    sleep(1000);
    robot.keyToggle('right', 'up');
}

function confirmTree(screen_x,screen_y) {
    robot.moveMouseSmooth(screen_x,screen_y,1);
    sleep(300);

    var check_x = 103;
    var check_y = 63; 

    var pixel_color = robot.getPixelColor(check_x,check_y);


    return pixel_color == "00ffff";
}



function sleep(ms) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

function getRandomInt(min, max) {
    // inclusive of min and max
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

main();