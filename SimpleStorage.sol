//SPDX-License-Identifier: MIT;
pragma solidity 0.6.0;

contract SimpleStorage {
    //this will initialized to 0//^0.6.0;

    uint256 public favouritenumber;
    bool favouriteBool;

    struct People {
        uint256 favouritenumber;  
        string name;
    }

    // people public person=people({favouritenumber:2,name: "jayakumar"});
    // newpeople[1] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    function store(uint256 _favouritenumber) public {
        favouritenumber = _favouritenumber;
        //  uint256 test =4;
    }

    function store2(uint256 number) public {
        favouritenumber = number;
    }

    function retrivestored_values() public view returns (uint256) {
        return favouritenumber;
    }

    function addPerson(string memory _name, uint256 _favoritenumber) public {
        //People.push(People(_favoritenumber,_name ));
        nameToFavouriteNumber[_name] = _favoritenumber;
    }
}
