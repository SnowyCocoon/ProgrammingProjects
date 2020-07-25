import 'phaser';

export default class PreloaderScene extends Phaser.Scene {
    constructor ()  {
        super('Preloader');
    }

    init(){
        this.readyCount =0;
    }

    preload(){
        this.timeEvent = this.time.delayedCall(1, this.ready, [], this)
        this.createPreloader();
        this.loadAssets();
    }

    loadAssets(){
        // load assets needed in our game
        this.load.image("bullet", 'src/assets/level/bulletDark2_outline.png');
        this.load.image("tower", 'src/assets/level/tank_bigRed.png');
        this.load.image("enemy", 'src/assets/level/tank_sand.png');
        this.load.image("base", 'src/assets/level/tankBody_darkLarge_outline.png');
        this.load.image("title", 'src/assets/ui/title.png');
        this.load.image("cursor", 'src/assets/ui/cursor.png');
        this.load.image("blueButton1", 'src/assets/ui/blue_button02.png');
        this.load.image("blueButton2", 'src/assets/ui/blue_button03.png');

        // placeholder
        this.load.image("logo2", 'src/assets/logo.png');

        // tilemap in JSON format
        this.load.tilemapTiledJSON('level1', 'src/assets/level/level1.json');
        this.load.spritesheet('terrainTiles_default', 'src/assets/level/terrainTiles_default.png', { frameWidth: 64, frameHeight: 64});
    }

    createPreloader(){
        var width = this.cameras.main.width;
        var height = this.cameras.main.height;

        //add logo
        this.add.image(width /2, height/2 - 100, 'logo')

        // display progress bar
        var progressBar = this.add.graphics();
        var progressBox = this.add.graphics();
        progressBox.fillStyle(0x222222, 0.8);
        progressBox.fillRect(width / 2 - 160, height /2 -30, 320, 50)


        //Loading Txt
        var loadingText = this.make.text({
            x: width /2,
            y: height /2 -50,
            text: 'Loading....',
            style: {
                font: '20px monospace',
                fill: '#ffffff'
            }
        });
        loadingText.setOrigin(0.5,0.5) //anchor in center

        //percent Txt
        var percentText = this.make.text({
            x: width /2,
            y: height /2 -5,
            text: '0%.',
            style: {
                font: '18px monospace',
                fill: '#ffffff'
            }
        });
        percentText.setOrigin(0.5,0.5) //anchor in center

        //Loading assets Txt
        var assetText = this.make.text({
            x: width /2,
            y: height /2 + 50,
            text: '',
            style: {
                font: '18px monospace',
                fill: '#ffffff'
            }
        });
        assetText.setOrigin(0.5,0.5) //anchor in center


        // update progress bar
        this.load.on('progress', function (value) {
            console.log(value);
            percentText.setText(parseInt(value * 100) + '%')
            progressBar.clear();
            progressBar.fillStyle(0xffffff, 1);
            progressBar.fillRect(width / 2 - 150, height /2 -20, 300 * value, 30)
        });

        //update file progress text
        this.load.on('fileprogress', function (file) {
            assetText.setText('Loading Asset: ' + file.key)
        });
            
        // remove progress when complete
        this.load.on('complete', function() {
            progressBar.destroy();
            progressBox.destroy();
            assetText.destroy();
            loadingText.destroy();
            percentText.destroy();
            this.ready();
        }.bind(this));

        //time event for logo
        //TODO - update dalayedCall time
        
    }

    ready(){
        this.readyCount++;
        if (this.readyCount === 2) {
            this.scene.start('Game');
        }
    }

    create(){

    }
}