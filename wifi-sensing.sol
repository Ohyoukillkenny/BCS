pragma solidity ^0.4.21;

contract SensingWifi{
    uint public rewardUnit;
    uint public rewardNum;
    uint public dataCount;
    bytes32 public wifiName;
    address public requester;
    enum State {Uncreated, Created, Inactive}
    State public state;

    // struct Data{
    //     bytes32 loc;
    //     int strength;
    // }
    // Data[] public dataCommits;

    mapping(bytes32 => string) dataStatuses; // Either '' or 'Committed'

    modifier condition(bool _condition) {
        require(_condition);
        _;
    }

    modifier onlyRequester() {
        require(msg.sender == requester);
        _;
    }

    modifier inState(State _state) {
        require(state == _state);
        _;
    }

    event Aborted();
    event TaskInited();
    event DataCommited(bytes32 l, bytes32 w, int s);
    event TaskDone();

    /// Init the task as requster.
    /// The requster need to set the value of reward for each sensing data,
    /// as well as the maximum number of data he needed.
    function initTask(uint _rewardUnit, uint _rewardNum, bytes32 _wifiName)
        public
        inState(State.Uncreated)
        condition(msg.value >= _rewardUnit * _rewardNum)
        payable
    {
        requester = msg.sender;
        rewardUnit = _rewardUnit;
        rewardNum = _rewardNum;
        wifiName = _wifiName;
        state = State.Created;
        emit TaskInited();
        
    }


    /// Abort the Task and reclaim the ether,
    /// Can only be called by the requester.
    function abort()
        public
        onlyRequester
        inState(State.Created)
    {
        require(dataCount <= rewardNum);
        state = State.Inactive;
        requester.transfer(this.balance);
        emit Aborted();
    }

    /// Worker answer the task by sending data
    /// such as {"41-24-12.2-N 2-10-26.5-E", "SJTU", -51}

    function commitTask(bytes32 _location, bytes32 _wifiName, int _signalDegree)
        public
        inState(State.Created)
    {
        require(dataCount < rewardNum);
        bytes memory sensingDataCommit = bytes(dataStatuses[_location]);
        // Requester wants to get data from different location
        require(sensingDataCommit.length == 0);
        
        // Make sure that the wifi signal sensed is what requester wants
        require(wifiName == _wifiName);
        
        // The theoretical maximum value of signal strength is -30 dBm
        require(_signalDegree < -30);
        
        // // restructure the sensing data
        // // save the new data into dataCommits
        // dataCommits.push(Data({
        //     loc: _location,
        //     strength: _signalDegree
        // }));
        dataStatuses[_location] = "Committed";
        
        dataCount += 1;
        if(dataCount == rewardNum){
            state = State.Inactive;
            requester.transfer(this.balance);
            emit TaskDone();
        }
        msg.sender.transfer(rewardUnit);
        emit DataCommited(_location, _wifiName, _signalDegree);
    }
}