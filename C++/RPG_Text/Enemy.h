/*
 * Enemy.h
 *
 *  Created on: 2018 M08 8
 *      Author: Dominik Strzałko
 */

#ifndef ENEMY_H_
#define ENEMY_H_

#include <iostream>

class Enemy {
public:
	Enemy(std::string,int,int);

	void CheckStats();


	void setName(std::string name) {EnemyName = name;}
	void setStrength() {EnemyStrength = EnemyLvl * EnemyDifficulty;} //można dodać int na wejście który będzie mnoznikiem lub obniżał dmg zależnie od pancerza i czarów?
	void setHP(int HP) {EnemyHP = HP;}
	void setMaxHP() {EnemyMaxHP = 10 * EnemyLvl * EnemyDifficulty;}
	void setLvl(int Lvl) {EnemyLvl = Lvl;}
	void setDifficulty(int Diff) { EnemyDifficulty = Diff;}

	std::string getName() {return EnemyName;}
	int getStrength() {return EnemyStrength;}
	int getHP() {return EnemyHP;}
	int getMaxHP() {return EnemyMaxHP;}
	int getLvl() {return EnemyLvl;}
	int getDifficulty() {return EnemyDifficulty;}


private:
	std::string EnemyName;
	int EnemyStrength;
	int EnemyHP;
	int EnemyMaxHP;
	int EnemyLvl;
	int EnemyDifficulty;
};

#endif /* ENEMY_H_ */
