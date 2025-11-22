// 2022184031 임수영
#include "Goal_WanderHealth.h"
#include "Goals/Goal_FollowPath.h"
#include "Goals/Goal_Wander.h"
#include "Raven_ObjectEnumerations.h"
#include "Goals/Raven_Feature.h"
#include "navigation/Raven_PathPlanner.h"
#include "Messaging/Telegram.h"
#include "Raven_Messages.h"

Goal_WanderHealth::Goal_WanderHealth(Raven_Bot* pBot)
    :Goal_Composite<Raven_Bot>(pBot, goal_wander_health)
{
    _visited = false;
}

void Goal_WanderHealth::Activate()
{
	m_iStatus = active;

	RemoveAllSubgoals();

    // 힐템 경로 찾기
    m_pOwner->GetPathPlanner()->RequestPathToItem(type_health);
    // 일단 배회
    AddSubgoal(new Goal_Wander(m_pOwner));
}

int Goal_WanderHealth::Process()
{
    ActivateIfInactive();

    // 배회 시작 거리
    float wanderDis = 0.2;
    // 배회하다 일정 거리 이상 멀어지면 다시 힐템 경로 찾을 거리
    float comebackDis = 0.4;
    // 힐템까지의 거리
    float itemDis = Raven_Feature::DistanceToItem(m_pOwner, type_health);

    if (itemDis > comebackDis && _visited)
    {
        _visited = false;

        // 힐템 근처로 다시 가기 위해 경로 찾기
        m_pOwner->GetPathPlanner()->RequestPathToItem(type_health);
        // 일단 배회
        RemoveAllSubgoals();
        AddSubgoal(new Goal_Wander(m_pOwner));
    }
    else if(itemDis <= wanderDis && !_visited)
    {
        _visited = true;
        RemoveAllSubgoals();
        AddSubgoal(new Goal_Wander(m_pOwner));
    }

    m_iStatus = ProcessSubgoals();
    return m_iStatus;
}

bool Goal_WanderHealth::HandleMessage(const Telegram& msg)
{
    switch (msg.Msg)
    {
    case Msg_PathReady:
        RemoveAllSubgoals();
        AddSubgoal(new Goal_FollowPath(m_pOwner, m_pOwner->GetPathPlanner()->GetPath()));
        return true;
    default: 
        return false;
    }
}