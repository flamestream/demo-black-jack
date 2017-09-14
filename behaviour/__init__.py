import behaviour.tryhard
import behaviour.dealer
import behaviour.human

tryhard = behaviour.tryhard.TryHardBehaviour()
dealer = behaviour.dealer.DealerBehaviour()
human = behaviour.human.HumanBehaviour()

__all__ = [tryhard, human, dealer]
