OptionMap(
    {
        "Debug Log File": Option(
            name="Debug Log File", type="string", default="", min=None, max=None, var=[]
        ),
        "Threads": Option(
            name="Threads", type="spin", default=1, min=1, max=1024, var=[]
        ),
        "Hash": Option(
            name="Hash", type="spin", default=16, min=1, max=33554432, var=[]
        ),
        "Clear Hash": Option(
            name="Clear Hash", type="button", default="", min=None, max=None, var=[]
        ),
        "Ponder": Option(
            name="Ponder", type="check", default=False, min=None, max=None, var=[]
        ),
        "MultiPV": Option(
            name="MultiPV", type="spin", default=1, min=1, max=500, var=[]
        ),
        "Skill Level": Option(
            name="Skill Level", type="spin", default=20, min=0, max=20, var=[]
        ),
        "Move Overhead": Option(
            name="Move Overhead", type="spin", default=10, min=0, max=5000, var=[]
        ),
        "Slow Mover": Option(
            name="Slow Mover", type="spin", default=100, min=10, max=1000, var=[]
        ),
        "nodestime": Option(
            name="nodestime", type="spin", default=0, min=0, max=10000, var=[]
        ),
        "UCI_Chess960": Option(
            name="UCI_Chess960", type="check", default=False, min=None, max=None, var=[]
        ),
        "UCI_AnalyseMode": Option(
            name="UCI_AnalyseMode",
            type="check",
            default=False,
            min=None,
            max=None,
            var=[],
        ),
        "UCI_LimitStrength": Option(
            name="UCI_LimitStrength",
            type="check",
            default=False,
            min=None,
            max=None,
            var=[],
        ),
        "UCI_Elo": Option(
            name="UCI_Elo", type="spin", default=1350, min=1350, max=2850, var=[]
        ),
        "UCI_ShowWDL": Option(
            name="UCI_ShowWDL", type="check", default=False, min=None, max=None, var=[]
        ),
        "SyzygyPath": Option(
            name="SyzygyPath",
            type="string",
            default="<empty>",
            min=None,
            max=None,
            var=[],
        ),
        "SyzygyProbeDepth": Option(
            name="SyzygyProbeDepth", type="spin", default=1, min=1, max=100, var=[]
        ),
        "Syzygy50MoveRule": Option(
            name="Syzygy50MoveRule",
            type="check",
            default=True,
            min=None,
            max=None,
            var=[],
        ),
        "SyzygyProbeLimit": Option(
            name="SyzygyProbeLimit", type="spin", default=7, min=0, max=7, var=[]
        ),
        "Use NNUE": Option(
            name="Use NNUE", type="check", default=True, min=None, max=None, var=[]
        ),
        "EvalFile": Option(
            name="EvalFile",
            type="string",
            default="nn-a3dc078bafc7.nnue",
            min=None,
            max=None,
            var=[],
        ),
    }
)
