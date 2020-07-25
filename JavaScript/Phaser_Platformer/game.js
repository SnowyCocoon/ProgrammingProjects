var config = {
    type: Phaser.AUTO,
    width: 1000,
    height: 750,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var player;
var stars;
var bombs;
var peach;
var platforms;
var cursors;
var score = 0;
var gameOver = false;
var scoreText;
var right = true; // left to false

var game = new Phaser.Game(config);

function preload ()
{
    this.load.image('peach', 'assets/brzoskwinka.png');
    this.load.image('jungle', 'assets/jungle.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', 'assets/Cherry.png');
    this.load.image('bomb', 'assets/bomb.png');
    this.load.spritesheet('banan', 'assets/Bananor.png', { frameWidth: 32, frameHeight: 36 });
}

function create ()
{
    //  A simple background for our game
    this.add.image(500, 375, 'jungle');

    //  The platforms group contains the ground and the 2 ledges we can jump on
    platforms = this.physics.add.staticGroup();

    //  Here we create the ground.
    //  Scale it to fit the width of the game (the original sprite is 400x32 in size)
    platforms.create(400, 568, 'ground').setScale(3).refreshBody();

    //  Now let's create some ledges
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');

    // The player and its settings
    player = this.physics.add.sprite(100, 450, 'banan');

    //  Player physics properties. Give the little guy a slight bounce.
    player.setBounce(0.2);
    player.setCollideWorldBounds(true);

    //  Our player animations, turning, walking left and walking right.
    this.anims.create({
        key: 'run_left',
        frames: this.anims.generateFrameNumbers('banan', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });
    this.anims.create({
        key: 'run_right',
        frames: this.anims.generateFrameNumbers('banan', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'idle_right',
        frames: [ { key: 'banan', frame: 4 } ],
        frameRate: 20
    });
    this.anims.create({
        key: 'idle_left',
        frames: [ { key: 'banan', frame: 12 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'jump_right',
        frames: [ { key: 'banan', frame: 9 } ],
        frameRate: 20
    });
    this.anims.create({
        key: 'jump_left',
        frames: [ { key: 'banan', frame: 10 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'death_right',
        frames: [ { key: 'banan', frame: 11 } ],
        frameRate: 20
    });
    this.anims.create({
        key: 'death_left',
        frames: [ { key: 'banan', frame: 13 } ],
        frameRate: 20
    });

    //  Input Events
    cursors = this.input.keyboard.createCursorKeys();

    //  Some stars to collect, 12 in total, evenly spaced 70 pixels apart along the x axis
    stars = this.physics.add.group({
        key: 'star',
        repeat: 13,
        setXY: { x: 12, y: 0, stepX: 70 }
    });

    stars.children.iterate(function (child) {

        //  Give each star a slightly different bounce
        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));

    });

    bombs = this.physics.add.group();

    //  The score
    scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: '#000' });

    //  Collide the player and the stars with the platforms
    this.physics.add.collider(player, platforms);
    this.physics.add.collider(stars, platforms);
    this.physics.add.collider(bombs, platforms);

    //  Checks to see if the player overlaps with any of the stars, if he does call the collectStar function
    this.physics.add.overlap(player, stars, collectStar, null, this);

    this.physics.add.collider(player, bombs, hitBomb, null, this);
}

function update ()
{
    if (gameOver)
    {
        return;
    }
    //Poruszanie się
    if (cursors.left.isDown)
    {
        player.setVelocityX(-160);
        right = false;
    }
    else if (cursors.right.isDown)
    {
        player.setVelocityX(160);
        right = true;
    }
    else if(player.body.touching.down)
    {
        player.setVelocityX(0);
    }
    if (cursors.up.isDown && player.body.touching.down)
    {
        player.setVelocityY(-330);
    }

    //Animacje
    if(cursors.left.isDown && player.body.touching.down)
    {
        player.anims.play('run_left', true);
    }
    else if(cursors.right.isDown && player.body.touching.down)
    {
        player.anims.play('run_right', true);
    }
    else if(cursors.left.isDown && !player.body.touching.down)
    {
        player.anims.play('jump_left');
    }
    else if(cursors.right.isDown && !player.body.touching.down)
    {
        player.anims.play('jump_right');
    }
    else if(player.body.touching.down && right)
    {
        player.anims.play('idle_right');
    }
    else if(player.body.touching.down && !right)
    {
        player.anims.play('idle_left');
    }



}

function collectStar (player, star)
{
    star.disableBody(true, true);

    //  Add and update the score
    score += 10;
    scoreText.setText('Score: ' + score);

    if (stars.countActive(true) === 0)
    {
        //  A new batch of stars to collect
        stars.children.iterate(function (child) {

            child.enableBody(true, child.x, 0, true, true);

        });

        var x = (player.x < 400) ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);

        var bomb = bombs.create(x, 16, 'bomb');
        bomb.setBounce(1);
        bomb.setCollideWorldBounds(true);
        bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);
        bomb.allowGravity = false;

    }
}

function hitBomb (player, bomb)
{
    this.physics.pause();

    player.setTint(0xff0000);

    if(right)
    {
        player.anims.play('death_right', true);
    }
    else
    {
        player.anims.play('death_left', true);
    }

    gameOver = true;
}