import unittest
from unittest.mock import patch
import badges

class PhoenixBadgeBoundaries(unittest.TestCase):
    def test_threshold_comparison_is_inclusive_only_when_requested(self):
        master='EQAZzZzhBdrPwxFVQHWlMHbDY_eOk3LeUPr07VWdX4B0193M'
        wallet='0:'+'1'*64
        def response(path):
            if path == '/jettons/'+master:
                return {'metadata':{'address':badges.raw_friendly(master),'decimals':'9'}}
            return {'total':1,'addresses':[{'balance':str(50000*10**9),'owner':{'address':wallet}}]}
        with patch.object(badges,'fetch',side_effect=response):
            self.assertEqual(badges.holders(master,False,50000),{})
            self.assertEqual(badges.holders(master,True,50000),{wallet:True})

    def test_jvault_sums_positions_by_owner_before_threshold(self):
        owner='0:'+'2'*64
        other='0:'+'3'*64
        amounts={'a':(owner,250000*10**9),'b':(owner,250000*10**9),'c':(other,500000*10**9-1)}
        with patch.object(badges,'discover',return_value=(set(amounts),42)),patch.object(badges,'position',side_effect=amounts.__getitem__),patch.object(badges.time,'sleep'):
            self.assertEqual(badges.stake({})['wallets'],{owner:True})

    def test_removed_jvault_is_not_refreshed(self):
        with patch.object(badges,'refresh_generic',return_value={'sources':{},'failed':[]}),patch.object(badges,'stake') as stake:
            result=badges.refresh({'sources':{'jvault':{'asOf':1}}},100000)
        stake.assert_not_called()
        self.assertNotIn('jvault',result['sources'])

if __name__=='__main__': unittest.main()
