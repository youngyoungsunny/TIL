솔리디티(영어: Solidity)는 계약 지향 프로그래밍 언어로 다양한 블록체인 플랫폼의 스마트계약(Smart Contract) 작성 및 구현에 사용된다.br/>
솔리디티는 Gavin Wood의 설계대로 ECMAScript 문법을 기반<br/>
솔리디티는 정적타입(statically-typed)의 프로그래밍 언어로 EVM상에서 작동하는 스마트계약을 개발하기 위해 설계되었다.<br/>
솔리디티는 EVM에서 작동가능한 바이트코드로 컴파일된다. 개발자는 솔리디티를 통해서 스스로 실행되는 비즈니스 로직을 스마트계약에 담아서 Application을 구현할 수 있다.<br/>


#Example of a Solidity program: <br/>
~~~sol

contract GavCoin
{
  mapping(address=>uint) balances;
  uint constant totalCoins = 100000000000;

  /// Endows creator of contract with 1m GAV.
  function GavCoin(){
      balances[msg.sender] = totalCoins;
  }

  /// Send $((valueInmGAV / 1000).fixed(0,3)) GAV from the account of $(message.caller.address()), to an account accessible only by $(to.address()).
  function send(address to, uint256 valueInmGAV) {
    if (balances[msg.sender] >= valueInmGAV) {
      balances[to] += valueInmGAV;
      balances[msg.sender] -= valueInmGAV;
    }
  }

  /// getter function for the balance
  function balance(address who) constant returns (uint256 balanceInmGAV) {
    balanceInmGAV = balances[who];
  }

}
~~~

개념 출처: https://ko.wikipedia.org/wiki/%EC%86%94%EB%A6%AC%EB%94%94%ED%8B%B0 <br/>
