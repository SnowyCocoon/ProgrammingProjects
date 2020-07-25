import 'phaser';
import map from '../config/map';
import Enemy from '../objects/Enemy';
import Turret from '../objects/Turret';

export default class GameScene extends Phaser.Scene {
    constructor ()  {
        super('Game');
    }

    init(){
        this.map = map.map(function (arr) {
            return arr.slice();
        });
        //console.log(this.map);
        this.nextEnemy = 0;
    }

    create(){
        this.createMap();
        this.createPath();
        this.createCursor();
        this.createGroups();
    }

    update(time, delta){
        if(time > this.nextEnemy){
            var enemy = this.enemies.getFirstDead();
            if (!enemy) {
                enemy = new Enemy(this,0,0, this.path);
                this.enemies.add(enemy);
            }
            if(enemy) {
                enemy.setActive(true);
                enemy.setVisible(true);

                enemy.startOnPath();

                this.nextEnemy = time + 2000
            }
        }
    }

    createGroups() {
        this.enemies = this.physics.add.group({classType: Enemy, runChildUpdate: true});
        this.turrets = this.add.group({classType: Turret, runChildUpdate: true});
        this.input.on('pointerdown', this.placeTurret.bind(this));
    }

    createCursor() {
        this.cursor = this.add.image(32, 32, 'cursor');
        this.cursor.setScale(2);
        this.cursor.alpha = 0;

        this.input.on('pointermove', function (pointer) {
            var i = Math.floor(pointer.y / 64);
            var j = Math.floor(pointer.x / 64);

            if (this.canPlaceTurret(i,j)){
                this.cursor.setPosition(j * 64 + 32, i * 64 + 32);
                this.cursor.alpha = 0.8;
            } else {
                this.cursor.alpha = 0;
            }
        }.bind(this));
    }
    canPlaceTurret(i, j){
        return this.map[i][j] === 0;
    }

    createPath() {
        this.graphics = this.add.graphics();
        // the path the enemies followe
        this.path = this.add.path(96, -32);
        this.path.lineTo(96,164);
        this.path.lineTo(480,164);
        this.path.lineTo(480,544);

        //visualizing the path
        this.graphics.lineStyle(3, 0xffffff, 1);
        this.path.draw(this.graphics);
    }

    createMap() {
        //create our map
        this.bgMap = this.make.tilemap({ key: 'level1'});
        //add tileset img
        this.tiles = this.bgMap.addTilesetImage('terrainTiles_default');
        // create our backgron layer
        this.backgroundLayer = this.bgMap.createStaticLayer('Background', this.tiles, 0, 0)
        // add tower
        this.add.image(480, 480, 'base');
    }

    getEnemy(){
        return false;
    }

    addBullet(){

    }

    placeTurret(pointer){
        var i = Math.floor(pointer.y / 64);
        var j = Math.floor(pointer.x / 64);

        if (this.canPlaceTurret(i,j)) {
            var turret = this.turrets.getFirstDead();
            if (!turret){
                turret = new Turret(this, 0,0,this.map);
                this.turrets.add(turret);
            }
            turret.setActive(true);
            turret.setVisible(true);
            turret.place(i,j);
            //TODO: turret limit
        }
    }
}