<?php

class Stack {

  public function __construct($list) {
    $this->stack = $list;
    $this->length = count($list);
  }

  public function empty_y(){
    if($this->length==0) return True;
    else return false;
  }

  public function T_peek(){
    return $this->stack[$this->length-1];
  }

  public function T_pop(){
    return $array_pop($this->stack);
  }

  public function T_push($value){
    array_push($this->stack, $value);
  }

  public function size(){
    return $this->length;
  }
}

?>
