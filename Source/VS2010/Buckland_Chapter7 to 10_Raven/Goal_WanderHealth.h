// 2022184031 ÀÓ¼ö¿µ
#include "Goals/Goal_Composite.h"
#include "Raven_Bot.h";

class Goal_WanderHealth : public Goal_Composite<Raven_Bot>
{
public:
	Goal_WanderHealth(Raven_Bot* pBot);

public:
	void Activate();
	int  Process();
	void Terminate() {}
	bool HandleMessage(const Telegram& msg);

private:
	bool _visited = false;
};