<?php

class Stack {

  public function __construct($list) {
    $this->stack = $list;
  }

  public function empty_y(){
    if(count($this->stack)==0) return True;
    else return False;
  }

  public function T_peek(){
    return $this->stack[count($this->stack)-1];
  }

  public function T_pop(){
    $s = $this->stack[count($this->stack)-1];
    array_pop($this->stack);
    return $s;
  }

  public function T_push($value){
    array_push($this->stack, $value);
  }

  public function size(){
    return count($this->stack);
  }
}

?>
