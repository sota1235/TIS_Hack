<?php

class Queue {

  public function __construct($list){
    require_once("./a.php");

    $this->stack = new Stack(array_reverse($list));
  }

  public function add($value){
    $this->stack->T_push($value);
  }

  public function T_peek(){
    $this->stack->T_peek();
  }

  public function T_remove(){
    $this->stack->T_remove();
  }

  public function size(){
    return $this->stack->size();
  }
}

?>
