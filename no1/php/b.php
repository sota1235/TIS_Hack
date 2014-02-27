<?php

class Queue {

  public function __construct($list){
    require_once("./a.php");

    $this->stack1 = new Stack($list);
    $this->stack2 = new Stack($list);
    while(!$this->stack1->empty_y()) $this->stack1->T_pop();
    for($i=0;$i<count($list);$i++){
      $this->stack1->T_push($this->stack2->T_pop());
    }
  }

  public function add($value){
    $this->stack1->T_push($value);
  }

  public function T_peek(){
    return $this->stack1->T_peek();
  }

  public function T_remove(){
    $this->stack1->T_remove();
  }

  public function size(){
    return $this->stack1->size();
  }
}

?>
