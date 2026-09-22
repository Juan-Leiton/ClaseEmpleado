
package relaciones_poo;

public class Empleado {
    
    public String Cargo;
    public String Nombre;
        
    public Empleado(String Nombre, String Cargo){
        this.Nombre = Nombre;
        this.Cargo = Cargo;
    }
        
    public String getNombre(){
        return Nombre;
    }
    
    public String getCargo(){
        return Cargo;
    }
        
    @Override
        
    public String toString(){
        return Nombre;
    }
}
