/*
 * Enemy.cpp
 *
 *  Created on: 2018 M08 8
 *      Author: Dominik Strzałko
 */

#include "Enemy.h"
#include <string>

Enemy::Enemy(std::string name, int lvl, int diff ) {
	setName(name);
	setLvl(lvl);
	setDifficulty(diff);
	setMaxHP();
	setHP(EnemyMaxHP);
	setStrength();
}

void Enemy::CheckStats() {
	std::cout << "These are your enemy stats: " << std::endl;
	std::cout << "Enemy Name: " << EnemyName << std::endl;
	std::cout << "Enemy Level: " << EnemyLvl << std::endl;
	std::cout << "Enemy Hitpoints: " << EnemyHP << std::endl;
	std::cout << "Enemy Strength: " << EnemyStrength << std::endl;
}