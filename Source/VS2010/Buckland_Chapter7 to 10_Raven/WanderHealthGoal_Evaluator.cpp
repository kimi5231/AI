// 2022184031 임수영
#include "WanderHealthGoal_Evaluator.h"
#include "Goals/Raven_Feature.h"
#include "Raven_ObjectEnumerations.h"
#include "Goals/Goal_Think.h"

double WanderHealthGoal_Evaluator::CalculateDesirability(Raven_Bot* pBot)
{
    // 힐템까지의 거리
    float itemDis = Raven_Feature::DistanceToItem(pBot, type_health);

    if (itemDis == 1)
        return 0;
    else
    {
        // 가까울수록 점수 높게 주기
        double desirability = 1 - itemDis;
        desirability *= m_dCharacterBias;
        Clamp(desirability, 0, 1);
        return desirability;
    }
}

void WanderHealthGoal_Evaluator::SetGoal(Raven_Bot* pBot)
{
    pBot->GetBrain()->AddGoal_WanderHealth();
}