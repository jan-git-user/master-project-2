jQuery(document).ready(function($){
    
    // Prdoduktbeschreibung ausklappen für alle Objekte der Klasse .MAccordionContent 
  	$(".MAccordionContent").attr("aria-hidden", "false");
    
    
    // Reihenfolge von Elementen beliebig anpassen
    $(".PageProduct-emailSeller").insertAfter("MTabs-content");
    
  });