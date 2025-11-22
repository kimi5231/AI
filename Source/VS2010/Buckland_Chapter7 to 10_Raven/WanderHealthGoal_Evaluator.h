// 2022184031 ÀÓ¼ö¿µ
#pragma once
#include "Goals/Goal_Evaluator.h"
#include "Raven_Bot.h"

class WanderHealthGoal_Evaluator : public Goal_Evaluator
{
public:
	WanderHealthGoal_Evaluator(double bias) : Goal_Evaluator(bias) {}

public:
	double CalculateDesirability(Raven_Bot* pBot);
	void  SetGoal(Raven_Bot* pBot);
	void RenderInfo(Vector2D Position, Raven_Bot* pBot) {};
};